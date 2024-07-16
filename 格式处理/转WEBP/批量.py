from PIL import Image
import os


def convert_images_to_webp(source_dir, output_dir):
    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        print("目录不存在！")
        os.makedirs(output_dir)
        print("创建目录成功！")

    # 遍历源目录中的所有文件
    for filename in os.listdir(source_dir):
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


source_directory = r'D:\Downloads\pixiv_image'
output_directory = r'E:\webp\pixiv'
convert_images_to_webp(source_directory, output_directory)
