from hr import read_time
from hr import read_voltage
import pytest

def test_read_time():
    test_time = read_time()
    assert test_time == 0

def test_read_voltage():
    test_voltage = read_voltage()
    assert test_voltage == -0.145


