import pytest
from src.apb.testing import testing_env


def test_testing_env():
    st = testing_env()

    assert isinstance(st, str)
