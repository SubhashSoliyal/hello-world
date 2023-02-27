def function_name_print(a,b,c,d,e):
    print (a,b,c,d,e)

def fun_args(nor,*args,**kwargs):
    print(type(args))
    print (nor)
    for items in args:
        print(items)
    # print(args[0])
    print("\n\nNOw I would Like to introduce some heroes\n")
    for key,value in kwargs.items():
        print( f"{key} is a {value}.")

har = ["harry", "rohan", "skillf", "hammad",
        "shivam","the programer","subhash","soliyal"]
normal = "this is a normal arguments and the students are:\n"
kw = {'rohan':"Monitor", 'Harry':"Fitness Instructor",
       'The Programer':"Coordinator",'sivam': "cook"}

# fun_args(*har,normal)
# fun_args(normal,*har)
# fun_args(normal)
fun_args(normal,*har,**kw)