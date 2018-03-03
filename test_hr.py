from hr import ECG
import pytest

test_data1 = ECG('test_data1.csv', './test_data/', 27)


# def test_read_time():
#     """tests that time values are correct
#     """
#     assert test_data1.ecg_time[0] == 0


def test_read_voltage():
    """tests that the voltage values are correct
    """
    assert test_data1.ecg_voltage[0] == -0.145


def test_min_voltage():
    """tests the minimum voltage
    """
    assert test_data1.voltage_extremes[0] == -0.68


def test_max_voltage():
    """tests the maximum voltage
    """
    assert test_data1.voltage_extremes[1] == 1.05


def test_voltage_tuple_size():
    """tests the tuple size
    """
    assert len(test_data1.voltage_extremes) == 2


def test_ecg_duration():
    """tests the duration of the ecg
    """
    assert test_data1.duration == 27.775


def test_count_beats():
    """tests the number of beats detected
    """
    assert test_data1.number_beats == 32


def test_mean_HR():
    """tests the calculation for mean HR
    """
    import numpy as np
    import math
    a = math.floor(test_data1.meanHR)
    assert a == 71


def test_hr_upper_limit():
    """tests the range for the mean heart rate
    """
    assert test_data1.meanHR < 150


def test_hr_lower_limit():
    """tests the range for the mean HR
    """
    assert test_data1.meanHR > 40


# def test_json_file():
#     """tests that there is information in the json file
#     """
#     import json
#     json.loads('./test_data/test1.json')
#     with pytest.raises(ImportError):
#         print('File not found')


def test_beats_time():
    assert len(test_data1.beats_time) == 32
