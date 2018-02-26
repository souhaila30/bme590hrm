from hr import read_data
from hr import read_time
from hr import read_voltage
from hr import ecg_plot
from hr import find_voltage_extremes
import pytest


ecg_data = read_data()


def test_read_time():
    test_time = read_time(ecg_data)
    assert test_time[0] == 0


def test_read_voltage():
    test_voltage = read_voltage(ecg_data)
    assert test_voltage [0] == -0.145


# def test_ecg_plot():
#     test_plot = ecg_plot([0,1,2,3,4],[0.1,0.2,0.3,0.4])
#


def test_min_voltage():
    test_min = find_voltage_extremes([-2,5,0,4,3,7])
    assert test_min[0] == -2


def test_max_voltage():
    test_max = find_voltage_extremes([786,904,12,-0.9])
    assert test_max[1] == 904


def test_voltage_tuple_size():
    test_tuple = find_voltage_extremes([0,9.3,5,6,-3,2])
    assert len(test_tuple) == 2


def test_ecg_duration():
    test_duration = find_ecg_duration([9,91,904,23,54,78,891,0,85])
    assert test_duration == 904



