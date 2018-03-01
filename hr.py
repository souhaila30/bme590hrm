class ECG:

    """class that reads an ECG data file, and determines mean HR
    """

    def __init__(self, file_type, relative_path):
        """Initializes the attributes of Read_ecg
        """

        self.relative_path = relative_path
        self.file_type = file_type
        self.input_path = "./test_data/test_data1.csv"
        self.ecg_data = []
        self.ecg_voltage = 0
        self.ecg_time = 0
        self.duration = 0
        self.voltage_extremes = 0
        #self.peaks = 0
        self.correlation = []
        self.main()

    import logging
    logging.basicConfig(filename='logging.txt',
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y & I:%M:%S %p',
                        level=logging.DEBUG)

    def read_data(self):

        """reads the data from the input files and returns the data read
        """
        import os
        self.input_path = os.path.join(self.relative_path,
                                       self.file_type)
        print('input file path:', self.input_path)
        import pandas as pd
        self.ecg_data = pd.read_csv(self.input_path, delimiter=',',
                                    header=None)
        return self.ecg_data

    def read_time(self):
        """finds the time in the ecg data read and returns the time

        :param ecg_data: time and voltage of the ecg data read
        :return: time of ecg data
        """
        self.ecg_time = self.ecg_data[0]
        print('ecg time')
        print(self.ecg_time)
        print('first time', self.ecg_time[0])
        return self.ecg_time

    def read_voltage(self):
        """finds the voltage of the ecg data and returns the voltage

        :param ecg_data:  input data including time and voltage
        :return: voltage of ecg data
        """
        self.ecg_voltage = self.ecg_data[1]
        print('ecg voltage')
        print(self.ecg_voltage)
        print('first voltage', self.ecg_voltage[0])
        return self.ecg_voltage

    def ecg_plot(self):
        """plots the ecg data in terms of time and voltage

        :param ecg_time: time input from the ecg
        :param ecg_voltage: voltage from the ecg
        :return: a plot of time vs. voltage
        """
        import matplotlib as mlp
        mlp.use('TkAgg')
        import matplotlib.pyplot as plt
        ecg_plot = plt.plot(self.ecg_time, self.ecg_voltage)
        plt.xlabel('time')
        plt.ylabel('voltage')
        plt.show ()
        return ecg_plot

    def find_voltage_extremes(self):
        """takes in the voltage data and returns the voltage extremes

        :param ecg_voltage:
        :return:
        """
        import numpy as np
        max_voltage = np.max(self.ecg_voltage)
        print('max voltage:', max_voltage)
        min_voltage = np.min(self.ecg_voltage)
        print('min voltage:', min_voltage)
        self.voltage_extremes = (min_voltage, max_voltage)
        print('voltage extremes:', self.voltage_extremes)
        return self.voltage_extremes

    def find_ecg_duration(self):
        """takes in ecg time and returns the duration

        :param: takes in ecg time
        :return: the duration
        """
        import numpy as np
        min_time = np.min(self.ecg_time)
        print('min time:', min_time)
        max_time = np.max(self.ecg_time)
        print('max time:', max_time)
        self.duration = max_time - min_time
        print('duration:', self.duration)
        return self.duration

    def autocorrelate(self):
        import numpy as np
        import matplotlib as mlp
        mlp.use('TkAgg')
        import matplotlib.pyplot as plt
        self.correlation = np.correlate (self.ecg_data[1], self.ecg_data[1],'full')
        print('ecg_data[1]',self.ecg_data[1])
        print('correlation results:', self.correlation)
        correlation_plot = plt.plot(self.correlation)
        plt.xlabel('time')
        plt.ylabel('correlation sum')
        plt.show()
        return correlation_plot
        return self.correlation

    # def find_peaks(self):
    #     """takes ecg data and finds the peaks
    #
    #     :param: takes in ecg data - time and voltage
    #     :return: location of peaks - maximum voltage
    #     """
    #     import pandas as pd
    #     import matplotlib as mlp
    #     mlp.use('TkAgg')
    #     #import matplotlib.gipyplot as plt
    #     import numpy as np
    #     import math


    def main(self):
        self.ecg_data = self.read_data()
        self.ecg_time = self.read_time()
        self.ecg_voltage = self.read_voltage()
        self.voltage_extremes = self.find_voltage_extremes()
        self.duration = self.find_ecg_duration()
        ecg_plot = self.ecg_plot()
        #self.peaks = self.find_peaks()
        self.correlation = self.autocorrelate()
        correlation_plot = self.autocorrelate()



if __name__ == "__main__":
    a = ECG('test_data1.csv', "./test_data/")
