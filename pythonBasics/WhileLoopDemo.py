it = 10

while it > 1:
    if it == 9:
        it = it - 1
        continue  # used to end the current iteration in a for loop (or a while loop),
        # and continues to the next iteration.
    if it == 3:
        break
    print(it)

    it = it - 1

print('While loop execution is done')
