# Classes are nothing but user defined blueprint or prototype
# sum, addition, multiplication, constant
# Methods, class variables, instance variables, constructor and so on
# objects for your classes
class Calculator:
    # class variables are created just inside the class level
    # class variables are constant, and they won't change.
    num = 100

    # when I create an object of this class, then a default constructor will be created and
    # attached to this class, the default constructor that will be created just like below:
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    # if I created variables via constructor, then that kind of variables are called instance level
    # variables, and they can be changed every time that I created an object from a class.
    def get_data(self):
        print("I am now executing as a method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + self.num
        # return self.firstNumber + self.secondNumber + Calculator.num


# the variables in parentheses are the instance level variables, so they can be changed
obj = Calculator(2, 3)  # syntax to create objects in python
obj.get_data()  # syntax to access methods in another object in python
print(obj.summation())  # we can access the class variable by this way.

obj1 = Calculator(4, 5)
obj.get_data()
print(obj1.summation())

# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be _init_
# new keyword is not required when you create a new object
