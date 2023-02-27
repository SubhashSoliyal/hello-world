# l = 10 #global veriable

# def function1(n):
#     # l =5 #local variable
#     m =8 #local variable
#     global l
#     l= l +45
#     print(l,m)
#     print(n, "I have printed")

# function1("this is me")
# print(l)
x= 89
def herry():
    x=20
    def rohan():
        global x
        x = 80
    print("befor calling rohan()", x)
    rohan()
    print("after calling rohan()",x)

herry()
print(x)