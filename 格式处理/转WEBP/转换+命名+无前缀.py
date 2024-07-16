from PIL import Image
import os


def rename_files(target_directory):
    # 获取目录下所有文件
    files = os.listdir(target_directory)

    # 过滤出所有图片文件
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

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
    return renamed_files


def convert_images_to_webp(source_dir, output_dir, files):
    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        print("目录不存在！")
        os.makedirs(output_dir)
        print("创建目录成功！")

    # 遍历指定的文件
    for filename in files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # 打开图片
            img_path = os.path.join(source_dir, filename)
            img = Image.open(img_path)

            # 转换为webp格式
            webp_filename = os.path.splitext(filename)[0] + '.webp'
            webp_path = os.path.join(output_dir, webp_filename)
            img.save(webp_path, 'webp')

            print(f"Converted {filename} to {webp_filename}")

    print("转换完成！")


# 设置路径和前缀
source_directory = r'D:\Downloads\pixiv_image'
output_directory = r'E:\webp\pixiv'

# 先重命名文件
renamed_files = rename_files(source_directory)

# 再转换文件格式
convert_images_to_webp(source_directory, output_directory, renamed_files)
