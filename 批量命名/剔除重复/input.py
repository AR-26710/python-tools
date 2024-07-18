from main import rename_images


# 从用户输入获取参数
directory = input("请输入要处理的文件夹路径: ")
prefix = input("请输入文件名前缀（可选）: ")
output_excel_dir = input("请输入Excel文件存放路径: ")
prefix_excel_name = input("请输入带前缀命名的Excel文件名: ")
no_prefix_excel_name = input("请输入不带前缀命名的Excel文件名: ")

# 调用重命名函数
rename_images(
    directory=directory,
    prefix=prefix,
    output_excel_dir=output_excel_dir,
    prefix_excel_name=prefix_excel_name,
    no_prefix_excel_name=no_prefix_excel_name
)
