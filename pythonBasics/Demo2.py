# mixed type of variables can be included in an array
values = [1, 2, "Rahul", 4, 5]
print(values[0])  # print out the first element of an array
print(values[1])
print(values[3])
print(values[-1])  # print out the last index of an array
print(values[1:3])  # print out the first and the second elements excluding the 3rd element

# push value to a list
values.insert(3, "Shetty")  # [1, 2, 'Rahul', 'Shetty', 4, 5]
print(values)
# Add a value in the end of the array
values.append("End")  # [1, 2, 'Rahul', 'Shetty', 4, 5, 'End']
print(values)
# replace or update a value in a specific index
values[2] = "RAHUL"
# deleting a value in a specific index
del values[0]
print(values)  # [2, 'RAHUL', 'Shetty', 4, 5, 'End']

# Tuple data type, just like list datatype, but it is immutable
val = (1, 2, "Rahul", 4.5)
print(val[1])

# val[2] = "RAHUL"  This one will not work, because the tuple datatype is immutable,
# so we can't change any value of any elements of it
print(val)

# Dictionary data type
dic = {"a": 2, 4: "abc", "c": "Hello World"}
print(dic[4])
print(dic["c"])

# How to create dictionary data type run time
dic1 = {}
dic1["firstname"] = "Rahul"
dic1["lastname"] = "Shetty"
dic1["gender"] = "Male"
print(dic1)
print(dic1["firstname"])
