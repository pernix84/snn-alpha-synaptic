# Import the code to be tested
# import validator

# Import the test framework
import pytest


# @pytest.fixture(name="Successful test", scope="session")
def test_success():
    assert 2 * 2 == 4


# @pytest.fixture(name="Failing test", scope="session")
def test_fail():
    assert 2 * 2 == 5
