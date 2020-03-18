import numpy as np


# dict1 = {}
# dict2 = {1: 'ajay', 2: 'sanjay', 3: 'vijay'}
# dict3 = {'name': 'ajay', 1: [3, 5]}
# dict4 = dict({1: 'ajay', 2: 'vijay'})
# dict5 = dict([(1, 'one'), (2, 'two')])
#
# print(dict1.values())
# print(dict2.keys())

# for item in range(1, 6):
#     printable = dict + item
#     print(printable)

# def check(my_list):
#     if len(my_list) is 0:
#         print('list is enpty')
#     else:
#         print('length of list is ', len(my_list))

# def check(listone):
#     if not listone:
#         print('khali hai')
#     else:
#         print('khali nahi hai')


# def check(listone):
#     return np.array(listone)


# check([0])


# getting unique values from list

# def get_unique(listone):
#     unique_list = []
#     for value in listone:
#         if value not in unique_list:
#             unique_list.append(value)
#     print(unique_list)

# def get_unique(listone):
#     list_set = set(listone)
#     return list(list_set)

# def get_unique(listone):
#     arr = np.array(listone)
#     return np.unique(arr)

# print(get_unique([10, 20, 10, 30, 40, 40]))


# def multiply(listone, value):
#     new_list = []
#     for item in listone:
#         new_list.append(item * value)
#     return new_list

# def multiply(listone, value):
#     arr = np.array(listone)
#     return arr * value


# def multiply_listitems(listone):
#     result = 1
#     for item in listone:
#         result = result * item
#     return result


def multiply_listitems(listone):
    arr = np.array(listone)
    return np.product(arr)


print(multiply_listitems([2, 9, 4]))
