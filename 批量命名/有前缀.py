import os


def rename_file(target_directory, file_prefix):
    # 遍历文件夹中的文件
    files = os.listdir(target_directory)
    files.sort()  # 按字母顺序排序文件

    # 重命名文件
    for i, file in enumerate(files, start=1):
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.webp'):
            old_path = os.path.join(target_directory, file)
            new_filename = f'{file_prefix}{str(i).zfill(3)}{os.path.splitext(file)[1]}'
            new_path = os.path.join(target_directory, new_filename)

            if os.path.exists(new_path):
                print(f'跳过重命名: {file}')
            else:
                os.rename(old_path, new_path)
                print(f'已重命名: {file} -> {new_filename}')
        else:
            print(f'跳过非图片文件: {file}')


path = r'E:\webp\pixiv'
prefix = 'pixiv-'

rename_file(path, prefix)
