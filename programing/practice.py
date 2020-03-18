# def testgen(index):
#     weekdays = ['mon', 'tue', 'wed', 'thr', 'fri', 'sat', 'sun']
#     yield weekdays[index]
#     yield weekdays[index + 1]
#
#
# day = testgen(0)
# print(next(day), next(day))
# # print(next(day))
# # print(next(day))


# weeklist = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# print(weeklist)
# # covert list into string
# print(''.join(weeklist))
# # convert list into set
# print(set(weeklist))
# # convert list into tuple
# print(tuple(weeklist))


# def scope_test():
#
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#
#     do_global()
#     print("After global assignment:", spam)
#
# scope_test()
# print("In global scope:", spam)



