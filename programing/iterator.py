# my_list = [4, 7, 0, 5]
#
#
# my_iter = iter(my_list)
#
# print(next(my_iter))
# print(next(my_iter))
#
# print(my_iter.__next__())
# print(my_iter.__next__())
#
# for item in my_list:
#     print(item)
#
#
# # How for loop actually works?
#
# def for_loop():
#     iter_obj = iter(my_list)
#     while True:
#         try:
#             element = next(iter_obj)
#             print(element)
#         except StopIteration:
#             break
#
#
# for_loop()


# user defined iterator

class PowerTwo:
    """Class to implement an iterator
       of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


iter_obj = PowerTwo(4)
my_iter = iter(iter_obj)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# for item in iter_obj:
#     print(item)

# while True:
#     try:
#         item = next(my_iter)
#         print(item)
#     except StopIteration:
#         break

