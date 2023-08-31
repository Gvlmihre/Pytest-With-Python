string = "RahulShettyAcademy.com"
string1 = "Consulting firm"
string2 = "RahulShetty"

print(string[1])  # a
print(string[0:5])  # Rahul
print(string + string1)  # Concatenation between two strings

# to check if a string present in another string we can do like this
print(string2 in string)

var = string.split(".")
print(var)
print(var[0])

string3 = " great "
print(string3)
# strip is a method that used to remove the white spaces in the beginning and end of a string
print(string3.strip())

# lstrip is a method that used to clear the white spaces on the left side of a string,
# the left side usually is the beginning of a string
print(string3.lstrip())
# rstrip is a method that used to remove the white spaces on the right side of a string,
# the right side usually is the end of a string
print(string3.rstrip())
