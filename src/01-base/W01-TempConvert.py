def temp_convert():
    """
    温度转换
    """
    TempStr = input("请输入带有符号的温度值: ")
    if TempStr[-1] in ['F', 'f']:
        C = (eval(TempStr[0:-1]) - 32) / 1.8
        print(f"转换后的温度是{C:.2f}C")
    elif TempStr[-1] in ['C', 'c']:
        F = 1.8 * eval(TempStr[0:-1]) + 32
        print(f"转换后的温度是{F:.2f}F")
    else:
        print("输入格式错误")


if __name__ == '__main__':
    temp_convert()
