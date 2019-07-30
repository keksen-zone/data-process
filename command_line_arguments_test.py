import sys
import getopt


def draw(argv):
    print(argv)
    if (argv[0] == "-x"):
        print("first para is x")
        x_pos = argv[1]
        print(x_pos)
        string_time = argv[2]
        print(string_time)
        string_attr = argv[3]
        print(string_attr)
        # 调用x
    elif (argv[0] == "-y"):
        print("first para is y")
    elif (argv[0] == "-z"):
        print("first para is z")
    else:
        print("输入参数错误")
        print("用法: xxx.py -x(-y,-z) x坐标 time(注意输入格式) 属性编号")
        print("示例: xxx.py -x 10.0 1.25187500E+07 0")
        sys.exit(2)


if __name__ == "__main__":
    draw(sys.argv[1:])
