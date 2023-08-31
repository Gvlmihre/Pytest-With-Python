from OopsDemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    # because the constructor in the parent class is not a default constructor,
    # and there are some codes, so I need to fix it firstly by adding the parent class
    # constructor in the child class constructor.
    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def get_complete_data(self):
        return self.num2 + self.num + self.summation()


# I start to create a new object of the child class
obj = ChildImpl()
print(obj.get_complete_data())
