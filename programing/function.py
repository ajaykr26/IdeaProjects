# Functions: A function is a block of organized, reusable code that is used to perform a single, related action.
# Functions provide better modularity and a high degree of code reusability.
# Syntax:
# def function_name(parameters):
#     '''function doc string '''
#     function suite
#     return expression
#
# Calling a function

# no argument function
# def fun_1():
#     """this is the function having no argument
#     and nothing to return"""
#     a, b = 3, 5
#     print(a, b)
#     print(a + b)
#
#
# print(fun_1())


# def fun_2(a, b): # variable argument function
#     """function with the parameters but no return """
#     print('variables are: ', 'a = ', a, ', b = ', b)
#     print('sumation is: ', a + b)
#
#
# fun_2(4, 7)  # positional argument
# fun_2(b=4, a=9)  # keyword argument position changed
# fun_2(a=10, b=2)  # keyword argument same position

# def fun_3(a=2, b=4):
#     """key value default parameters"""
#     print('variables are: ', 'a = ', a, ', b = ', b)
#     print(a + b)
#
#
# fun_3()  # calling with default parameters
# fun_3(4, 6)  # calling with different parameters assigning to default positional arguments
# fun_3(b=3, a=6)  # calling with different parameters assigning to positional arguments changed
# fun_3(a=10, b=40)  # calling with different parameters assigning to positional arguments same

# def fun_4(a, b):  # function which return object
#     return a + b
#
#
# print(fun_4(3, 7))


# def fun_5(arg, *args):  # function with variable arguments
#     print(arg, args)  # *args stored in a tuple
#     print(arg, args[0], args[1], args[2])
#
#
# fun_5(4, 5, 6, 'ajay')

# def fun_6(**kwargs):  # function with variable key-value arguments
#     print(kwargs)  # **kwargs stored in the dict
#     print(kwargs['first'])
#     for key, value in kwargs.items():
#         print("%s : %s" % (key, value))
#
#
# fun_6(first='Geeks', mid='for', last='Geeks')


# def fun_6(firstname, **kwargs):
#     print(firstname)
#     print(kwargs)
#     for key, value in kwargs.items():
#         print("%s : %s" % (key, value))
#
#
# fun_6('ajay')
# fun_6(firstname = 'ajay', lastname = 'kumar', company = 'accenture', address='gurgaon')


# Here, we are maintaining reference of the passed object and appending values in the same object.


# def changeme(arg):
#     """This changes a passed list into this function"""
#     list_2 = [1, 2, 3, 4]
#     print("list inside the function: ", list_2)
#     return arg.append(list_2);
#
#
# # Now you can call changeme function
# list_1 = [10, 20, 30];
# print("list outside the function: ", list_1)
#
# changeme(list_1);
# print("final list: ", list_1)


# def changeme(arg):
#     """This changes a passed list into this function"""
#     arg = [1, 2, 3, 4];  # This would assign to the name arg
#     print("Values inside the function: ", arg)
#     return
#
#
# # Now you can call changeme function
# list_1 = [10, 20, 30];
# changeme(list_1);
# print("Values outside the function: ", list_1)

# Function definition is here lamda function
# def total(arg1, arg2): return arg1 + arg2;
#
#
# print("Value of total : ", total(10, 20))
# print("Value of total : ", total(20, 20))


# method and function:
# method: inside the class,

# def fun(name):
#     print('I am executing function', name)
#
#
# class MyClass:
#
#     def __init__(self, name):
#         self.name = name
#
#     def method_name(self):
#         """this is method under class"""
#         print('I am executin method which is in the class', self.name)
#
#
# obj = MyClass('method')
# obj.method_name()
# fun('function')

# *****************************
# recursive function: Recursion is the process of defining something in terms of itself. function calling itself
# Advantages of Recursion
# Recursive functions make the code look clean and elegant.
# A complex task can be broken down into simpler sub-problems using recursion.
# Sequence generation is easier with recursion than using some nested iteration.

# Disadvantages of Recursion
# Sometimes the logic behind recursion is hard to follow through.
# Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
# Recursive functions are hard to debug.

# find the factorial of integer
# def cal_factorial(x):
#     """This is a recursive function
#         to find the factorial of an integer"""
#     if x == 1:
#         return 1
#     else:
#         return x * cal_factorial(x - 1)
#
#
# print(cal_factorial(5))


# *****************************lamda function************************************
# lamda function: function that is defined without a name
# syntax: lambda arguments: expression

# ex
# multiplication = lambda x, y: x * y
# print(multiplication(3,5))

# use: We use lambda functions when we require a nameless function for a short period of time.

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# print(new_list)


# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(map(lambda x: x * 2 , my_list))
# print(new_list)

# ***************************** Python Global, Local and Nonlocal variables*****************************8

# variable declared outside of the function or in global scope is known as global variable.
# global variable can be accessed inside or outside of the function.

# Example 1: Create a Global Variable
# variable = 'global'
#
#
# def fun(): print('local scope inside the function: ', variable)
#
#
# fun()
# print('global scope outside the function: ', variable)


# variable = 'global'
#
#
# def fun():
#     global variable
#     newvariable = variable * 2
#     print('local scope inside the function: ', newvariable)
#
#
# fun()
# print('global scope outside the function: ', variable)

# local variable: declared inside the function's body or in the local scope is known as local variable.
# def fun():
#     variable = 'local'
#     print('local scope inside the function: ', variable)
#
#
# fun()


# Global variable and Local variable with same name
x = 5


def fun():
    x = 10
    print("local x:", x)


fun()
print("global x:", x)
