import os


def rename_file(target_directory):
    # 获取目录下所有文件
    files = os.listdir(target_directory)

    # 过滤出所有图片文件
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', 'webp'))]

    # 按照数字升序重命名图片文件
    renamed_files = []
    for i, file in enumerate(sorted(image_files), 1):
        # 构造新文件名
        _, ext = os.path.splitext(file)
        new_name = f"{i:03d}{ext}"

        # 检查新文件名是否已经存在
        if os.path.exists(os.path.join(target_directory, new_name)):
            print(f'命名文件已存在，跳过: {new_name}')
            renamed_files.append(new_name)
            continue

        # 重命名文件
        os.rename(os.path.join(target_directory, file), os.path.join(target_directory, new_name))
        print(f'已重命名: {file} -> {new_name}')
        renamed_files.append(new_name)

    print("图片文件已按照数字升序重命名。")


# 指定要重命名的目录
directory_path = r'E:\webp\pixiv'

# 调用函数进行重命名
rename_file(directory_path)
