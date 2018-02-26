def read_data():
    import pandas as pd
    ecg_data = pd.read_csv('./test_data/test_data1.csv', delimiter=',', header=None)
    return ecg_data

def read_time(ecg_data):
    ecg_time = ecg_data[0]
    print(ecg_time)
    print(ecg_time[0])
    return ecg_time

def read_voltage(ecg_data):
    ecg_voltage = ecg_data[1]
    print(ecg_voltage)
    print(ecg_voltage[0])
    return ecg_voltage

def ecg_plot(ecg_time,ecg_voltage):
    import matplotlib as mlp
    mlp.use('TkAgg')
    import matplotlib.pyplot as plt
    plt.plot(ecg_time, ecg_voltage)
    plt.xlabel('time')
    plt.ylabel('voltage')
    plot = plt.show ()
    return plot

def find_voltage_extremes(ecg_voltage):
    import numpy as np
    max_voltage = np.max(ecg_voltage)
    print(max_voltage)
    min_voltage = np.min(ecg_voltage)
    print(min_voltage)
    voltage_extremes = (min_voltage, max_voltage)
    print(voltage_extremes)
    return voltage_extremes

def main():
    ecg_data = read_data()
    ecg_time = read_time(ecg_data)
    ecg_voltage = read_voltage(ecg_data)
    plot = ecg_plot(ecg_time, ecg_voltage)
    voltage_extremes = find_voltage_extremes(ecg_voltage)

if __name__ == "__main__":
    main()
