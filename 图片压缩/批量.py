import os
import time
from PIL import Image


def compress_image(input_image_path, output_image_path, quality):
    try:
        # 打开输入图像
        image = Image.open(input_image_path)

        # 压缩并保存图像
        image.save(output_image_path, "JPEG", quality=quality)
        print(f"Image saved to {output_image_path} with quality={quality}")
    except Exception as e:
        print(f"Failed to compress {input_image_path}: {e}")


def compress_images_in_directory(input_directory, output_directory, quality):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    start_time = time.time()

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_directory):
        input_image_path = os.path.join(input_directory, filename)

        # 检查文件是否为图像文件（可以根据需要修改）
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            output_image_path = os.path.join(output_directory, filename)
            compress_image(input_image_path, output_image_path, quality)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"压缩完毕，最终耗时{elapsed_time:.2f} 秒")


input_path = r"E:\迅雷下载\蠢沫沫253套合集130G\蠢沫沫 No.064 黄豆粉 [140P-850MB]"
output_path = r"E:\迅雷下载\蠢沫沫253套合集130G\蠢沫沫 No.064 黄豆粉 [140P-850MB]\output"
image_quality = 50  # 质量从1（最差）到95（最好）

compress_images_in_directory(input_path, output_path, image_quality)
