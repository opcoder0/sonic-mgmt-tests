import pytest

from fixtures.conftest import setup

def test_fixtures(setup):
    print("Test")
    assert True