import os
import hashlib
from collections import defaultdict
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from tkinter import ttk


# 计算文件的哈希值
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
def find_duplicate_files(directory, progress_var, progress_bar):
    """
    在给定目录及其子目录中查找重复的文件。

    :param directory: 开始搜索的目录。
    :param progress_var: 进度条变量。
    :param progress_bar: 进度条部件。
    :return: 一个字典，键为文件的哈希值，值为具有相同哈希值的文件路径列表。
    """
    file_list = []
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_list.append(file_path)

    total_files = len(file_list)
    hashes = defaultdict(list)

    for i, file_path in enumerate(file_list):
        file_hash = calculate_hash(file_path)
        hashes[file_hash].append(file_path)
        progress_var.set((i + 1) / total_files * 100)
        progress_bar.update_idletasks()

    return {hash_val: file_list for hash_val, file_list in hashes.items() if len(file_list) > 1}


# 处理重复的文件
def handle_duplicates(duplicates, action='delete', target_directory=None, progress_var=None, progress_bar=None):
    """
    对找到的重复文件执行指定的操作。

    :param duplicates: 一个字典，包含重复文件的详细信息。
    :param action: 对重复文件执行的操作，可以是'delete'（删除）或'move'（移动）。
    :param target_directory: 如果是'move'，则为目标目录的路径。
    :param progress_var: 进度条变量。
    :param progress_bar: 进度条部件。
    """
    total_files = sum(len(file_list) - 1 for file_list in duplicates.values())
    processed_files = 0

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
            processed_files += 1
            progress_var.set(processed_files / total_files * 100)
            progress_bar.update_idletasks()


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

    progress_window = tk.Toplevel(root)
    progress_window.title("进度")
    tk.Label(progress_window, text="正在查找重复文件...").pack(pady=10)
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(progress_window, length=300, variable=progress_var, maximum=100)
    progress_bar.pack(pady=10)
    progress_window.update()

    duplicates = find_duplicate_files(dir_to_search, progress_var, progress_bar)

    tk.Label(progress_window, text="正在处理重复文件...").pack(pady=10)
    progress_var.set(0)
    handle_duplicates(duplicates, action=action_to_take, target_directory=target_dir, progress_var=progress_var,
                      progress_bar=progress_bar)

    progress_window.destroy()
    messagebox.showinfo("完成", "重复文件处理完成！")


if __name__ == '__main__':
    main()
