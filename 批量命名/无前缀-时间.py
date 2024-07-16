import os
import shutil


def rename_file(target_directory, output_directory):
    # 获取目录下所有文件
    files = os.listdir(target_directory)

    # 过滤出所有图片文件
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', 'webp'))]

    # 按文件修改时间排序
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(target_directory, x)))

    # 确保输出目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 按照时间顺序重命名图片文件并复制到输出目录
    renamed_files = []
    for i, file in enumerate(image_files, 1):
        # 构造新文件名
        _, ext = os.path.splitext(file)
        new_name = f"{i:03d}{ext}"
        new_path = os.path.join(output_directory, new_name)

        # 检查新文件名是否已经存在
        if os.path.exists(new_path):
            print(f'命名文件已存在，跳过: {new_name}')
            renamed_files.append(new_name)
            continue

        # 复制并重命名文件
        shutil.copy2(os.path.join(target_directory, file), new_path)
        print(f'已重命名并复制: {file} -> {new_name}')
        renamed_files.append(new_name)

    print("图片文件已按照时间顺序重命名并复制到输出目录。")


# 指定要重命名的目录和输出目录
directory_path = r'D:\Pictures\pixiv'
output_path = r'D:\Pictures\pixiv\output'

# 调用函数进行重命名和复制
rename_file(directory_path, output_path)
