import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_first_program(setup):
    print('Hello')
    msg = "Hello"
    assert msg == "Hi", "Test failed, because strings do not match! "


def test_second_program(setup):
    a = 4
    b = 6
    assert a + 2 == 6, "Addition is right"
    print(a + 2)


