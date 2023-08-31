import pytest


# if I want to run the fixture in the class level just one before all the test cases and just after
# all the test cases in the class, then I can define the scope in the fixture as class, then I can
# reach my aim.
@pytest.fixture(scope="class")
def setup():
    print("I will be executing firstly")
    yield
    print("I will be executed last")


@pytest.fixture()
def data_load():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "Rahul", "Shetty"), ("Firefox", "Shetty"), ("IE", "SS")])
def cross_browser(request):
    return request.param

