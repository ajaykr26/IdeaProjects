# oops: inheritance, polymorphism, encapsulation, abstraction
# inheritance: single level inheritance, multi level inheritance, hierarchical inheritance, multiple inheritance
# class: A class is a blueprint for the third.We can think of class as an sketch of a parrot with labels.
# It contains all the details about the name, colors, size etc.
# Based on these descriptions, we can study about the parrot. Here, parrot is an third.

# third: An third (instance) is an instantiation of a class.
# When class is defined, only the description for the third is defined. Therefore, no memory or storage is allocated.
# Example 1: Creating Class and Object in Python


# class Parrot:
#     # class attribute
#     species = "bird"
#
#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# blu = Parrot("Blu", 10)  # instantiation of the Parrot class i.e creating third of parrot class
# woo = Parrot("Woo", 15)  # instantiation of the Parrot class i.e creating third of parrot class
#
# # accessing the class attributes
# print("Blu is a {}".format(blu.__class__.species))
# print("Woo is a {}".format(woo.__class__.species))
#
# # accessing the instance attributes
# print("{} is {} years old".format(blu.name, blu.age))
# print("{} is {} years old".format(woo.name, woo.age))


# method: functions defined inside the body of a class. They are used to define the behaviors of an third.
# Example 2 : Creating Methods in Python

# class Parrot:
#
#     # instance attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # instance method
#     def sing(self, song):
#         return "{} is now {}".format(self.name, song)
#
#     def dance(self):
#         return "{} is now dancing".format(self.name)
#
#
# # instantiate the third
# blu = Parrot("Blu", 10)
#
# # call our instance methods
# print(blu.sing("singing"))
# print(blu.dance())


# inheritance: Inheritance is a way of creating new class for using details of existing class without modifying it.
# The newly formed class is a child class. Similarly, the existing class is a parent class.
# single level inheritance, multi level inheritance, hierarchical inheritance, multiple inheritance

# Example 3: Use of Inheritance in Python
# single level inheritance
# parent class
# class ParentClass:
#     # class attribute
#     species = "animals"
#
#     def __init__(self):
#         print("this is instantiation of parent class")
#
#     def common_method(self):
#         print("this is overriden method in parent class")
#
#     @staticmethod
#     def parent_method_one(arg):
#         print("this is static method in parent class: ", arg)
#
#
# # child class
# class ChildClass(ParentClass):
#     # class attribute
#     animal = "dogs"
#
#     def __init__(self):
#         # call super() function
#         super().__init__()
#         # super(ChildClass, self).__init__()
#         print("this is instantiation of child class")
#
#     def common_method(self):
#         print("this is overriding method in child class")
#
#     @staticmethod
#     def child_method_one(arg):
#         print("this is static method in child class: ", arg)
#
#
# parent = ParentClass()
# print(parent.species)
# parent.common_method()
# parent.parent_method_one('parent')
#
# child = ChildClass()
# print(child.species, child.animal)
# child.common_method()
# child.child_method_one('child')


# multi level inheritance
# first class
# class FirstClass:
#     # class attribute
#     first_attribute = "first attribute"
#
#     def __init__(self):
#         print("this is instantiation of first class")
#
#     # def common_method(self):
#     #     print("this is overriden method in first class")
#
#     @staticmethod
#     def first_method_one(arg):
#         print("this is static method in first class: ", arg)
#
#
# # second class
# class SecondClass(FirstClass):
#     # class attribute
#     second_attribute = "second attribute"
#
#     def __init__(self):
#         # call super() function
#         # super().__init__()
#         super(SecondClass, self).__init__()
#         print("this is instantiation of second class")
#
#     def common_method(self):
#         print("this is overriding method in second class")
#
#     @staticmethod
#     def second_method_one(arg):
#         print("this is static method in second class: ", arg)
#
#
# # third class
# class ThirdClass(SecondClass):
#     # class attribute
#     third_attribute = "third attribute"
#
#     def __init__(self):
#         # call super() function
#         # super().__init__()
#         super(ThirdClass, self).__init__()
#         print("this is instantiation of third class")
#
#     def common_method(self):
#         print("this is overriding method in third class")
#
#     @staticmethod
#     def third_method_one(arg):
#         print("this is static method in third class: ", arg)
#
#
# third = ThirdClass()
# print(third.first_attribute, third.second_attribute, third.third_attribute)
# third.first_method_one('first')
# third.second_method_one('second')
# third.third_method_one('third')
# third.common_method()

# multiple inheritance
# first class
# class FirstClass:
#     # class attribute
#     first_attribute = "first attribute"
#
#     def __init__(self):
#         print("this is instantiation of first class")
#
#     def common_method_one(self):
#         print("this is overriden method in first class")
#
#     @staticmethod
#     def first_method_one(arg):
#         print("this is static method in first class: ", arg)
#
#
# # second class
# class SecondClass:
#     # class attribute
#     second_attribute = "second attribute"
#
#     def __init__(self):
#         # call super() function
#         # super().__init__()
#         super(SecondClass, self).__init__()
#         print("this is instantiation of second class")
#
#     def common_method_two(self):
#         print("this is overriding method in second class")
#
#     @staticmethod
#     def second_method_one(arg):
#         print("this is static method in second class: ", arg)
#
#
# # third class
# class ThirdClass(FirstClass, SecondClass):
#     # class attribute
#     third_attribute = "third attribute"
#
#     def __init__(self):
#         # call super() function
#         super(ThirdClass, self).__init__()
#         print("this is instantiation of third class")
#
#     def common_method_one(self):
#         print("this is overriding method in first class")
#
#     def common_method_two(self):
#         print("this is overriding method in second class")
#
#     @staticmethod
#     def third_method_one(arg):
#         print("this is static method in third class: ", arg)
#
#
# third = ThirdClass()
# print(third.first_attribute, third.second_attribute, third.third_attribute)
# third.first_method_one('first')
# third.second_method_one('second')
# third.third_method_one('third')
# third.common_method_one()
# third.common_method_two()


# hierarchical inheritance
# first class
# class FirstClass:
#     # class attribute
#     first_attribute = "first attribute"
#
#     def __init__(self):
#         print("this is instantiation of first class")
#
#     def common_method_one(self):
#         print("this is overriden method in first class")
#
#     @staticmethod
#     def first_method_one(arg):
#         print("this is static method in first class: ", arg)
#
#
# # second class
# class SecondClass(FirstClass):
#     # class attribute
#     second_attribute = "second attribute"
#
#     def __init__(self):
#         # call super() function
#         # super().__init__()
#         super(SecondClass, self).__init__()
#         print("this is instantiation of second class")
#
#     def common_method_one(self):
#         print("this is overriding method in second class")
#
#     @staticmethod
#     def second_method_one(arg):
#         print("this is static method in second class: ", arg)
#
#
# # third class
# class ThirdClass(FirstClass):
#     # class attribute
#     third_attribute = "third attribute"
#
#     def __init__(self):
#         # call super() function
#         super(ThirdClass, self).__init__()
#         print("this is instantiation of third class")
#
#     def common_method_one(self):
#         print("this is overriding method in first class")
#
#     @staticmethod
#     def third_method_one(arg):
#         print("this is static method in third class: ", arg)
#
#
# third = ThirdClass()
# second = SecondClass()
# print(third.first_attribute, third.third_attribute)
# print(second.first_attribute, second.second_attribute)
# second.first_method_one('second')
# third.first_method_one('third')
# second.common_method_one()
# third.common_method_one()




