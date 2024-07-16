def format_string(x, z, y):
    """
    根据输入的前缀、路径和终止数字，生成格式化后的字符串输出。

    参数:
    x -- 前缀字符串，可以为空
    z -- 路径字符串，可以为空
    y -- 终止数字，必须是1到999之间的整数

    Raises:
    ValueError -- 如果y不在1到999之间，则抛出此异常

    输出:
    格式化后的markdown格式字符串，用于表示文件名，输出类型如下：
    单空prefix
    ![001.webp](/upload/path/001.webp)
    单空path
    ![prefix-001.webp](/upload/prefix-001.webp)
    双空
    ![001.webp](/upload/001.webp)
    不空
    ![prefix-001.webp](/upload/path/prefix-001.webp)
    """
    # 将y转换为整数并验证其范围
    y = int(y)
    if y < 1 or y > 999:
        raise ValueError("终止数字y必须在1到999之间")

    # 遍历从1到y的每个数字，并格式化为三位数字符串
    for i in range(1, y + 1):
        formatted_number = f"{i:03}"
        # 根据前缀x和路径z，生成文件名和路径
        file_name = f"{x}-{formatted_number}.webp" if x else f"{formatted_number}.webp"
        z_path = f"/upload/{z}/{file_name}" if z else f"/upload/{file_name}"
        # 根据文件名和路径，生成markdown格式的字符串
        output = f"![{file_name}]({z_path})"
        print(output)


# 从用户输入获取前缀、路径和终止数字
prefix = input("请输入前缀的值（可为空）：")
path = input("请输入路径的值（可为空）：")
last = input("请输入终止数字（必须有）：")

# 调用format_string函数，根据用户输入生成格式化字符串输出
format_string(prefix, path, last)
