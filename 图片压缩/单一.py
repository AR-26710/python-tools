from PIL import Image


def compress_image(input_image_path, output_image_path, quality):
    # 打开输入图像
    image = Image.open(input_image_path)

    # 压缩并保存图像
    image.save(output_image_path, "JPEG", quality=quality)
    print(f"Image saved to {output_image_path} with quality={quality}")


input_path = r"E:\迅雷下载\蠢沫沫253套合集130G\蠢沫沫 No.064 黄豆粉 [140P-850MB]\001.jpg"
output_path = r"E:\迅雷下载\蠢沫沫253套合集130G\蠢沫沫 No.064 黄豆粉 [140P-850MB]\output\001.jpg"
imag_quality = 50  # 质量从1（最差）到95（最好）

compress_image(input_path, output_path, imag_quality)
