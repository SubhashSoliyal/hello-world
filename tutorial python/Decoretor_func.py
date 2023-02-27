# def function1():
#     print("subscribe now")

# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
    
# a = funcret(1)
# print(a)


def executor(func):
    func("this")

# executor(print)
# @executor
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

# @dec1
def how_is_herry():
    print("herry is a good boy")

how_is_herry = dec1(how_is_herry)
how_is_herry()


