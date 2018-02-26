def read_data():

    """

    reads the data from the input files and returns the data read

    """
    import pandas as pd
    ecg_data = pd.read_csv('./test_data/test_data1.csv', delimiter=',', header=None)
    return ecg_data


def read_time(ecg_data):
    """

    finds the time in the ecg data read and returns the time

    :param ecg_data: time and voltage of the ecg data read
    :return: time of ecg data

    """
    ecg_time = ecg_data[0]
    print(ecg_time)
    print(ecg_time[0])
    return ecg_time


def read_voltage(ecg_data):
    """

    finds the voltage of the ecg data and returns the voltage

    :param ecg_data:  input data including time and voltage
    :return: voltage of ecg data

    """
    ecg_voltage = ecg_data[1]
    print(ecg_voltage)
    print(ecg_voltage[0])
    return ecg_voltage


def ecg_plot(ecg_time,ecg_voltage):
    """

    plots the ecg data in terms of time and voltage

    :param ecg_time: time input from the ecg
    :param ecg_voltage: voltage from the ecg
    :return: a plot of time vs. voltage

    """
    import matplotlib as mlp
    mlp.use('TkAgg')
    import matplotlib.pyplot as plt
    plt.plot(ecg_time, ecg_voltage)
    plt.xlabel('time')
    plt.ylabel('voltage')
    plot = plt.show ()
    return plot


def find_voltage_extremes(ecg_voltage):
    """

    :param ecg_voltage:
    :return:
    """
    import numpy as np
    max_voltage = np.max(ecg_voltage)
    print(max_voltage)
    min_voltage = np.min(ecg_voltage)
    print(min_voltage)
    voltage_extremes = (min_voltage, max_voltage)
    print(voltage_extremes)
    return voltage_extremes


def find_ecg_duration(ecg_time):
    import numpy as np
    min_time = np.min(ecg_time)
    print(min_time)
    max_time = np.max(ecg_time)
    print(max_time)
    duration = max_time - min_time
    print(duration)
    return duration


def main():
    ecg_data = read_data()
    ecg_time = read_time(ecg_data)
    ecg_voltage = read_voltage(ecg_data)
    plot = ecg_plot(ecg_time, ecg_voltage)
    voltage_extremes = find_voltage_extremes(ecg_voltage)
    duration = find_ecg_duration(ecg_time)


if __name__ == "__main__":
    main()
