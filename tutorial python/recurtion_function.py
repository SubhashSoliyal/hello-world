# def print2(str1):
#     # print2(str1)
#     print("This is "+ str1)

# print2("Hello")

def factorial_itretive(n):
    fac = 1
    for i in  range(n):
        fac = fac * (i+1)
    '''
    :parm n: integer
    :return: n*n-1*n-2*.......1
    n! = n*n-1*n-2*.......1
    n! = n*(n-1)!
    '''
    return fac

def Factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * Factorial_recursive(n-1)


def Fibonacci(n):
    # 0 1 1 2 3 5 8 13 ......
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        return Fibonacci(n-1)+ Fibonacci(n-2)


number = int(input("Enter the no.: "))
print("Factor using iterative Method ",factorial_itretive(number))
print("Factor using recursive Method ",Factorial_recursive(number))
print("fibonacci number at this position ",Fibonacci(number))

