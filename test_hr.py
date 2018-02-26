from hr import read_data
from hr import read_time
from hr import read_voltage
import pytest


ecg_data = read_data()


def test_read_time():
    test_time = read_time(ecg_data)
    assert test_time[0] == 0


def test_read_voltage():
    test_voltage = read_voltage(ecg_data)
    assert test_voltage [0] == -0.145




