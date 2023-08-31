items_in_cart = 0
# 2 items should be added to the cart

if items_in_cart != 2:
    # I can use raise an exception to know the result of failing like below:
    # raise Exception("Products Cart Count Not Match Exception!")
    pass  # does nothing

assert (items_in_cart == 0)

# try, catch
# we use try catch block to prevent our tests from failing

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print("Some how I reached this block because there is a failure in try block")

try:
    with open('test.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

# Codes in the finally block will always be executed no matter there is an exception or not
# This message is always be printing no matter the test fails or not
finally:
    print("Cleaning up resources")
