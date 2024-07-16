import os
import shutil


def rename_file(target_directory, output_directory, file_prefix, overwrite=False):
    """
    重命名目标目录中的图片文件，并将它们复制到输出目录或进行覆盖。

    参数:
    target_directory: 字符串，源图片文件所在的目录。
    output_directory: 字符串，重命名后的图片文件将复制到这个目录。
    file_prefix: 字符串，重命名后的文件名将添加这个前缀。
    overwrite: 布尔值，如果为True，则重命名后的文件将覆盖输出目录中已存在的文件；如果为False，则不会覆盖。
    """

    # 遍历文件夹中的文件
    files = os.listdir(target_directory)
    # 过滤出jpg、png和webp格式的图片文件
    files = [f for f in files if f.endswith(('.jpg', '.png', '.webp'))]  # 过滤图片文件

    # 按时间顺序排序文件
    files.sort(key=lambda x: os.path.getmtime(os.path.join(target_directory, x)))

    # 确保输出目录存在（如果需要）
    if not overwrite and not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 遍历排序后的文件列表，重命名并复制到输出目录
    for i, file in enumerate(files, start=1):
        old_path = os.path.join(target_directory, file)
        # 构造新文件名
        new_filename = f'{file_prefix}{str(i).zfill(3)}{os.path.splitext(file)[1]}'
        # 根据是否覆盖文件，确定新文件路径
        new_path = os.path.join(output_directory if not overwrite else target_directory, new_filename)

        # 如果新文件已存在，则跳过当前文件
        if os.path.exists(new_path):
            print(f'跳过重命名: {file}')
        else:
            # 根据是否覆盖文件，选择重命名或复制文件
            if overwrite:
                os.rename(old_path, new_path)
                print(f'已重命名并覆盖: {file} -> {new_filename}')
            else:
                shutil.copy2(old_path, new_path)
                print(f'已重命名并复制: {file} -> {new_filename}')

    print("图片文件已按照时间顺序重命名并复制到输出目录。" if not overwrite else "图片文件已按照时间顺序重命名并覆盖原文件。")


# 指定源目录、输出目录和文件名前缀
# 指定要重命名的目录和输出目录
directory_path = r'D:\Pictures\pixiv'
output_path = r'D:\Pictures\pixiv\output'
prefix = 'pixiv-'


# 指定是否覆盖已存在的文件
overwrite_files = True  # True表示覆盖原文件，False表示输出到指定目录

# 调用函数执行重命名操作
rename_file(directory_path, output_path, prefix, overwrite=overwrite_files)
