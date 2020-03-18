# import sys
#
# if len(sys.argv) != 2:
#     raise ValueError('Please provide email-id to send the email.')
# print(f'Script Name is {sys.argv[0]}')
# email = sys.argv[1]
# print(f'Sending test email to {email}')

# import getopt
# import sys
# argv = sys.argv[1:]
# opts, args = getopt.getopt(argv, 'x:y:')
# # list of options tuple (opt, value)
# print(f'Options Tuple is {opts}')
# # list of remaining command-line arguments
# print(f'Additional Command-line arguments list is {args}')

# 3. Parsing Command-line arguments using argparse module
# We can use Python argparse module also to parse command-line arguments.
# There are a lot of options with argparse module.
#
# positional arguments
# the help message
# the default value for arguments
# specifying the data type of argument and many more.

# import argparse
#
# # create parser
# parser = argparse.ArgumentParser()
#
# # add arguments to the parser
# parser.add_argument("language")
# parser.add_argument("name")
#
# # parse the arguments
# args = parser.parse_args()
#
# # get the arguments value
# if args.language == 'Python':
#     print("I love Python too")
# else:
#     print("Learn Python, you will like it")
#
# print(f'Hello {args.name}, this was a simple introduction to argparse module')