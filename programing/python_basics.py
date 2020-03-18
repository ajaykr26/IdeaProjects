import os
import sys
import pathlib

# passing runtime arguments
# for arg in sys.argv:
#     print(arg)
print('filename: ', sys.argv[0])
print('name: ', sys.argv[1])
print('age: ', sys.argv[2])
print('company: ', sys.argv[3])
print('location: ', sys.argv[4])
# getting current working dir
print('current working dir: ', os.getcwd())
print('current working dir: ', pathlib.Path.cwd())
print('current working dir: ', pathlib.Path.home())
