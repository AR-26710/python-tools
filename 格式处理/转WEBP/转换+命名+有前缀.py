from PIL import Image
import os


def rename_files(target_directory, file_prefix):
    # 遍历文件夹中的文件
    files = os.listdir(target_directory)
    files.sort()  # 按字母顺序排序文件

    renamed_files = []

    # 重命名文件
    for i, file in enumerate(files, start=1):
        if file.lower().endswith(('.jpg', '.png', '.jpeg')):
            old_path = os.path.join(target_directory, file)
            new_filename = f'{file_prefix}{str(i).zfill(3)}{os.path.splitext(file)[1]}'
            new_path = os.path.join(target_directory, new_filename)

            # 如果新命名文件已存在则跳过
            if os.path.exists(new_path):
                print(f'命名文件已存在，跳过: {new_filename}')
                renamed_files.append(new_filename)
                continue

            os.rename(old_path, new_path)
            print(f'已重命名: {file} -> {new_filename}')
            renamed_files.append(new_filename)
        else:
            print(f'跳过非图片文件: {file}')

    return renamed_files


def convert_images_to_webp(source_dir, output_dir, files):
    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        print("目录不存在，正在创建目录！")
        os.makedirs(output_dir)
        print("创建目录成功！")

    # 遍历指定的文件
    for filename in files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(source_dir, filename)
            if not os.path.exists(img_path):
                print(f'文件不存在，跳过: {filename}')
                continue

            img = Image.open(img_path)

            # 转换为webp格式
            webp_filename = os.path.splitext(filename)[0] + '.webp'
            webp_path = os.path.join(output_dir, webp_filename)
            img.save(webp_path, 'webp')

            print(f"已转换: {filename} -> {webp_filename}")

    print("转换完成！")


# 设置路径和前缀
source_directory = r'D:\Downloads\pixiv_image'
output_directory = r'E:\webp\pixiv'
prefix = 'pixiv-'

# 先重命名文件
renamed_files = rename_files(source_directory, prefix)

# 再转换文件格式
convert_images_to_webp(source_directory, output_directory, renamed_files)
