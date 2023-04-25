

class Test1:
    def __init__(self):
        self.test = [Test2(), Test2()]

    def doSome(self, my_class, *args):
        print(my_class)
        t = my_class(*args)
        t.doOther()
        print(self.test)
        print(t)


class Test2:
    def __init__(self):
        print(123456)

    def doOther(self):
        print(654321)


if __name__ == '__main__':
    test = Test1()
    test.doSome(Test2)

    list1 = [1, 2, 3, 4, 5, 6]
    pos1, pos2 = 2, 5
    list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
    print(list1)
