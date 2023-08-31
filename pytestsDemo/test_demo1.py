# Any pytest file should start with test_ or and with _test
# pytest method names should start with test
# Any code should be wrapped in the method only
# Method name should have sense
# -k (keyword I guess) stands for method names execution, -s logs in out put, -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m(stands for mark)
# you can skip test with @pytest.mark.skip
# you can use @pytest.mark.xfail to not to run the test but report in the reports with xpass not with failure.
# fixtures are used as setup and teardown methods for test cases - conftest file to generalize
# fixture and make it available for all the test cases
# datadriven and parametrization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end
import pytest


@pytest.mark.smoke
def test_first_program(setup):
    print('Hello')


@pytest.mark.xfail
def test_greet_creditcard(setup):
    print('Good Morning!')


# to attach this method to that specific fixture, we need to pass the fixture name as an argument
def test_cross_browser(cross_browser):
    print(cross_browser[1])



