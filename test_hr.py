from hr import ECG
import pytest


# ecg_data = ECG.read_data(self)
test_data1 = ECG('test_data1.csv', './test_data/')

def test_read_time():
    assert test_data1.ecg_time[0] == 0


def test_read_voltage():
    assert test_data1.ecg_voltage [0] == -0.145


def test_min_voltage():
    #test_min = ECG.find_voltage_extremes([-2,5,0,4,3,7])
    assert test_data1.voltage_extremes[0] == -0.68


def test_max_voltage():
    #test_max = ECG.find_voltage_extremes([786,904,12,-0.9])
    #assert test_max[1] == 904
    assert test_data1.voltage_extremes[1] == 1.05


def test_voltage_tuple_size():
    # test_tuple = ECG.find_voltage_extremes([0,9.3,5,6,-3,2])
    # assert len(test_tuple) == 2
    assert len(test_data1.voltage_extremes) == 2

def test_ecg_duration():
    # test_duration = ECG.find_ecg_duration([9,91,904,23,54,78,891,0,85])
    # assert test_duration == 904
    assert test_data1.duration == 27.775

