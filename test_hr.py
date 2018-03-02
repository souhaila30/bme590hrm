from hr import ECG
import pytest

test_data1 = ECG('test1.csv', './test_data/',2)


def test_read_time():
    assert test_data1.ecg_time[0] == 0


def test_read_voltage():
    assert test_data1.ecg_voltage[0] == 0.2


def test_min_voltage():
    assert test_data1.voltage_extremes[0] == -0.6


def test_max_voltage():
    assert test_data1.voltage_extremes[1] == 1


def test_voltage_tuple_size():
    assert len(test_data1.voltage_extremes) == 2


def test_ecg_duration():
    assert test_data1.duration == 10


def test_count_beats():
    assert test_data1.number_beats == 1


def test_mean_HR():
    assert test_data1.meanHR == 60


def test_hr_upper_limit():
    assert test_data1.meanHR < 150


def test_hr_lower_limit():
    assert test_data1.meanHR > 2

