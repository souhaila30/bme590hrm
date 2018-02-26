
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

def main():
    ecg_data = read_data()
    ecg_time = read_time(ecg_data)
    ecg_voltage = read_voltage(ecg_data)

if __name__ == "__main__":
    main()
