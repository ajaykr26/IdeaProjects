# data types: number, string , list, dictionary, tuple, set

# number: int, float, complex

num_int = 124789
num_float = 6.12345678901234567890  # A floating point number is accurate up to 15 decimal places.
num_complex = 7 + 3j
print(num_int, num_float, num_complex)
print(type(num_int), type(num_float), type(num_complex))
print(isinstance(num_int, int), isinstance(num_float, float), isinstance(num_complex, complex))


# # type conversion
# # int to string, float, complex
# print(str(num_int), float(num_int), complex(num_int))
#
# # float to int, string, complex
# print(str(num_float), int(num_float), complex(num_float))
#
# # complex ca not be converted but we can get real and img part
# print(num_complex.real, num_complex.imag)

# my_string = 'hello: ajay'
#
# my_string = "hello"
# print(my_string)
#
# my_string = '''Hello, welcome to
# the world of Python'''
# print(my_string)
#
# my_string = """Hello, welcome to
# the world of Python"""
# print(my_string)


# # making string mutable
# my_string = 'computer'
# item = []
# for letter in my_string:
#     item.append(letter)
# # new_item = item[:3]
# item[4]='o'
# print("".join(item))


# Implicit Type Conversion
# Explicit Type Conversion


# python output
# name = 'ajay', 'sanjay'
# age = 45, 60
#
# print(name, end="\n")
# print(age, end="\n")
# print(name, file=open("C:/Users/Ajay Kumar/PycharmProjects/python-learning/resources/datafile.txt", "w"))
#
# print(age, end="\n",
#       file=open("C:/Users/Ajay Kumar/PycharmProjects/python-learning/resources/datafile.txt", "a"))

# formating
# name = 'ajay'; age = 30
# print('my name is {} and age is {}'.format(name, age))
# print('my name is {name} and age is {age}'.format(name = 'ajay', age = 30))

# python input : input([prompt])

# name = input('enter yor name\n')
# print('ohh you are {}'.format(name))
# print('you are of {age}'.format(age = input('enter your age\n')))

# bitwise operator: AND &, OR |, NOT ~, RINGHT SHIFT >>, LEFT SHIFT <<, XOR ^

# x = 10  # (0000 1010)
# y = 4  # (0000 0100)
# print(x & y)  # (0000 0000)
# print(x | y)  # (0000 1110)
# print(~ x)  # (1111 0101)
# print(x ^ y)  # (0000 1110)
# print(x >> 2)  # (0000 0010)
# print(x >> 3)  # (0000 0001)
# print(x >> 4)  # (0000 0000)
# print(x << 2)  # (0010 1000)

