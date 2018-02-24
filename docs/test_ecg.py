import numpy as np

def test_read_time():

    """

    tests that the  time is read properly from the file

    """

    test_time = read_time()
    assert test_time == time


def test_mean_hr_bpm():

    """

    tests the estimated average heart rate over a peiod of time

    """

    test_mean = find_mean_hr([34,60,56])
    assert test_mean == mean_hr


