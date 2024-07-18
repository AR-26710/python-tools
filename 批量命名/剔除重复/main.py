import os

import pandas as pd


def rename_images(directory, prefix='', output_excel_dir='./', start_num=0,
                  prefix_excel_name='with_prefix.xlsx', no_prefix_excel_name='no_prefix.xlsx'):
    """
    重命名目录中的图片文件，并记录重命名前后的情况到Excel表格。

    :param directory: 图片文件所在的目录
    :param prefix: 为图片文件添加的前缀
    :param output_excel_dir: 保存Excel表格的目录
    :param start_num: 图片文件重命名的起始编号
    :param prefix_excel_name: 包含加前缀的图片重命名记录的Excel文件名
    :param no_prefix_excel_name: 包含不加前缀的图片重命名记录的Excel文件名
    """
    # 创建输出目录如果它不存在
    if not os.path.exists(output_excel_dir):
        os.makedirs(output_excel_dir)

    # 构建Excel文件的完整路径
    excel_prefix_path = os.path.join(output_excel_dir, prefix_excel_name)
    excel_no_prefix_path = os.path.join(output_excel_dir, no_prefix_excel_name)

    # 如果Excel文件不存在，则创建一个空的DataFrame并保存
    if not os.path.exists(excel_prefix_path):
        df = pd.DataFrame(columns=['old_name', 'new_name'])
        df.to_excel(excel_prefix_path, index=False)

    if not os.path.exists(excel_no_prefix_path):
        df = pd.DataFrame(columns=['old_name', 'new_name'])
        df.to_excel(excel_no_prefix_path, index=False)

    # 读取已存在的Excel表格，如果没有则创建一个空的DataFrame
    df_prefix = pd.read_excel(excel_prefix_path) if os.path.exists(excel_prefix_path) else pd.DataFrame(columns=['old_name', 'new_name'])
    df_no_prefix = pd.read_excel(excel_no_prefix_path) if os.path.exists(excel_no_prefix_path) else pd.DataFrame(columns=['old_name', 'new_name'])

    # 获取已存在文件名的集合，用于检查新生成的文件名是否重复
    existing_prefix_names = set(df_prefix['new_name'].tolist())
    existing_no_prefix_names = set(df_no_prefix['new_name'].tolist())

    new_rows_prefix = []
    new_rows_no_prefix = []

    # 遍历目录中的文件，重命名并记录
    for i, filename in enumerate(os.listdir(directory), start=start_num):
        old_path = os.path.join(directory, filename)
        # 检查是否是文件，避免重命名目录
        if os.path.isfile(old_path):
            file_ext = os.path.splitext(filename)[1]  # 获取文件扩展名
            # 根据是否使用前缀，生成新文件名
            if prefix:
                new_name = generate_unique_name(prefix, i, existing_prefix_names, file_ext)
                new_rows_prefix.append({'old_name': filename, 'new_name': new_name})
            else:
                new_name = generate_unique_name('', i, existing_no_prefix_names, file_ext)
                new_rows_no_prefix.append({'old_name': filename, 'new_name': new_name})

            # 重命名文件
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)

    # 将新重命名的文件记录追加到Excel表格中
    if new_rows_prefix:
        df_prefix = pd.concat([df_prefix, pd.DataFrame(new_rows_prefix)], ignore_index=True)

    if new_rows_no_prefix:
        df_no_prefix = pd.concat([df_no_prefix, pd.DataFrame(new_rows_no_prefix)], ignore_index=True)

    # 保存更新后的Excel表格
    df_prefix.to_excel(excel_prefix_path, index=False)
    df_no_prefix.to_excel(excel_no_prefix_path, index=False)


def generate_unique_name(prefix, num, existing_names, file_ext):
    """
    生成唯一的文件名。

    :param prefix: 文件名前缀
    :param num: 文件编号
    :param existing_names: 已存在的文件名集合
    :param file_ext: 文件扩展名
    :return: 唯一的文件名
    """
    while True:
        new_name = f"{prefix}{num:06d}{file_ext}"
        # 检查新文件名是否重复，如果不重复则返回
        if new_name not in existing_names:
            existing_names.add(new_name)
            return new_name
        num += 1
