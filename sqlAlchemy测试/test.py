class a:
    i = 0

    def __init__(self):
        #python中静态成员变量要用类名来引用！
        print(a.i)
        a.i += 1
        print(a.i)

b = a()
c = a()
