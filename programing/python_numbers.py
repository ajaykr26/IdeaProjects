# number: int, float, complex

num_int = 124789
num_float = 6.12  # A floating point number is accurate up to 15 decimal places.
num_complex = 7 + 3j
print(num_int, num_float, num_complex)
print(type(num_int), type(num_float), type(num_complex))
print(isinstance(num_int, int), isinstance(num_float, float), isinstance(num_complex, complex))

# While integers can be of any length, a floating point number is accurate only up to 15 decimal places

# Numbers we deal with everyday are decimal (base 10) number system.
# But computer programmers (generally embedded programmer) need to work with binary (base 2), hexadecimal (base 16)
# and octal (base 8) number systems.

print(0B110110)
print(0XFB + 0B10)
print(0O15)
