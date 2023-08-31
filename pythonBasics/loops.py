greeting = "Good Morning"
if greeting == "Good Morning":
    print("Condition Matches")
    print("Second Line")
else:
    print("Condition don't match")
print("If else condition code is completed")

a = 4
if a > 2:
    print("Condition Matches")
    print("Second Line")
else:
    print("Condition don't match")
print("If else condition code is completed")

# for loop
obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

# sum of first natural numbers 1+2+3+4+5 = 15
# range(i,j) means it will iterate from i to j-1
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

print("**********************************")
for k in range(1, 10, 2):  # 2 in the curly bracket is the value that will be added in each step
    print(k)
print("*************SKIPPING FIRST INDEX*********************")
for m in range(10):  # if I don't define the starting value, then the default beginning value is zero
    print(m)
