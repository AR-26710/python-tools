from main import rename_images

# 设置重命名参数
directory = r"E:\python-tools\流萤"
prefix = "image-"
output_excel_dir = r"E:\python-tools\excel"
prefix_excel_name = "image_with_prefix.xlsx"
no_prefix_excel_name = "image_no_prefix.xlsx"

# 调用重命名函数
rename_images(
    directory=directory,
    prefix=prefix,
    output_excel_dir=output_excel_dir,
    prefix_excel_name=prefix_excel_name,
    no_prefix_excel_name=no_prefix_excel_name
)
