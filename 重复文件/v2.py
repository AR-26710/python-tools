import os
import hashlib
from collections import defaultdict
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog


def calculate_hash(file_path, hash_algo=hashlib.sha256):
    """
    计算给定文件的哈希值。

    :param file_path: 文件的路径。
    :param hash_algo: 哈希算法的函数，默认为sha256。
    :return: 文件的哈希值的十六进制字符串。
    """
    hash_obj = hash_algo()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# 查找重复的文件
def find_duplicate_files(directory):
    """
    在给定目录及其子目录中查找重复的文件。

    :param directory: 开始搜索的目录。
    :return: 一个字典，键为文件的哈希值，值为具有相同哈希值的文件路径列表。
    """
    hashes = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_hash(file_path)
            hashes[file_hash].append(file_path)
    return {hash_val: file_list for hash_val, file_list in hashes.items() if len(file_list) > 1}

# 处理重复的文件
def handle_duplicates(duplicates, action='delete', target_directory=None):
    """
    对找到的重复文件执行指定的操作。

    :param duplicates: 一个字典，包含重复文件的详细信息。
    :param action: 对重复文件执行的操作，可以是'delete'（删除）或'move'（移动）。
    :param target_directory: 如果是'move'，则为目标目录的路径。
    """
    for file_list in duplicates.values():
        for file_path in file_list[1:]:
            if action == 'delete':
                os.remove(file_path)
                print(f'Deleted: {file_path}')
            elif action == 'move' and target_directory:
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)
                new_path = os.path.join(target_directory, os.path.basename(file_path))
                os.rename(file_path, new_path)
                print(f'Moved: {file_path} to {new_path}')
            else:
                print(f'No action taken for: {file_path}')

def main():
    root = tk.Tk()
    root.withdraw()

    dir_to_search = filedialog.askdirectory(title="选择要搜索的目录")
    if not dir_to_search:
        messagebox.showerror("错误", "必须选择一个目录")
        return

    action_to_take = simpledialog.askstring("选择操作", "请输入操作（delete 或 move）:")
    if action_to_take not in ['delete', 'move']:
        messagebox.showerror("错误", "无效的操作，必须是 'delete' 或 'move'")
        return

    target_dir = None
    if action_to_take == 'move':
        target_dir = filedialog.askdirectory(title="选择目标目录")
        if not target_dir:
            messagebox.showerror("错误", "必须选择一个目标目录")
            return

    duplicates = find_duplicate_files(dir_to_search)
    handle_duplicates(duplicates, action=action_to_take, target_directory=target_dir)

if __name__ == '__main__':
    main()
