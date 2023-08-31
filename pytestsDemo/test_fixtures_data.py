import pytest


@pytest.mark.usefixtures("data_load")
class TestExample2:

    # If I need to use data from a fixture then I need to pass the fixture
    # name as one of the parameters in the test method
    def test_edit_profile(self, data_load):
        print(data_load[0])
        print(data_load[1])
        print(data_load[2])
