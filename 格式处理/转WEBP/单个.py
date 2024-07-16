from PIL import Image
import os

def convert_image_to_webp(image_path, output_dir):
    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        print("目录不存在！")
        os.makedirs(output_dir)
        print("创建目录成功！")

    if os.path.exists(image_path):
        # 检查文件扩展名是否是支持的图片格式
        if image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            # 打开图片
            img = Image.open(image_path)

            # 获取文件名和扩展名
            filename = os.path.basename(image_path)
            # 转换为webp格式
            webp_filename = os.path.splitext(filename)[0] + '.webp'
            webp_path = os.path.join(output_dir, webp_filename)
            img.save(webp_path, 'webp')

            print(f"Converted {filename} to {webp_filename}")
        else:
            print("文件格式不支持！")
    else:
        print("图片文件不存在！")


image_path = r'D:\Pictures\pixiv\120528579_p0_master1200.jpg'
output_directory = r'E:\webp\pixiv'
convert_image_to_webp(image_path, output_directory)
