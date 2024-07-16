import os
import shutil


def rename_file(target_directory, output_directory, file_prefix):
    # 遍历文件夹中的文件
    files = os.listdir(target_directory)
    files = [f for f in files if f.endswith(('.jpg', '.png', '.webp'))]  # 过滤图片文件

    # 按时间顺序排序文件
    files.sort(key=lambda x: os.path.getmtime(os.path.join(target_directory, x)))

    # 确保输出目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 重命名文件
    for i, file in enumerate(files, start=1):
        old_path = os.path.join(target_directory, file)
        new_filename = f'{file_prefix}{str(i).zfill(3)}{os.path.splitext(file)[1]}'
        new_path = os.path.join(output_directory, new_filename)

        if os.path.exists(new_path):
            print(f'跳过重命名: {file}')
        else:
            shutil.copy2(old_path, new_path)
            print(f'已重命名并复制: {file} -> {new_filename}')
        print(f'跳过非图片文件: {file}')


# 指定要重命名的目录和输出目录
directory_path = r'D:\Pictures\pixiv'
output_path = r'D:\Pictures\pixiv\output'
prefix = 'pixiv-'

# 调用函数进行重命名和复制
rename_file(directory_path, output_path, prefix)
