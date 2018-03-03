class ECG:
    """class that reads an ECG data file, and determines mean HR
    """

    def __init__(self, file_type, relative_path, user_input):
        """Initializes the attributes of ECG

        """

        self.relative_path = relative_path
        self.file_type = file_type
        self.input_path = "./test_data/test_data1.csv"
        self.user_input = user_input
        self.idx = 0
        self.ecg_data = []
        self.ecg_data_sliced = []
        self.ecg_voltage = 0
        self.ecg_time = 0
        self.duration = 0
        self.voltage_extremes = 0
        self.correlation = 0
        self.peaks = 0
        self.number_beats = 0
        self.meanHR = 0
        self.beats_time = []
        self.json_output = 'test_data1.json'
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
        try:
            self.ecg_data = pd.read_csv(self.input_path, delimiter=',',
                                        header=None)
        except ImportError:
            raise ImportError('File not found, input an new path')

        return self.ecg_data

    def read_time(self):
        """finds the time in the ecg data read and returns the time

        :param ecg_data: time and voltage of the ecg data read
        :return: time of ecg data
        """
        import numpy as np
        ecg_time = self.ecg_data[0]
        max_time = np.max(ecg_time)
        if self.user_input > max_time:
            raise ValueError("The time requested is longer "
                             "than the max time recorded")
        else:
            nearest_time = [abs(i - self.user_input) for i in ecg_time]
            self.idx = nearest_time.index(min(nearest_time))
            # print('index:',self.idx)
            self.ecg_time = ecg_time[:self.idx]
            self.ecg_data_sliced = self.ecg_data[:self.idx]
            # print(self.ecg_time)

        return self.ecg_time, self.idx, self.ecg_data_sliced

    def read_voltage(self):
        """finds the voltage of the ecg data and returns the voltage

        :param:  input data including time and voltage
        :return: voltage of ecg data
        """

        # ecg_data_sliced = self.ecg_data[:self.idx]
        # print(ecg_data_sliced)
        self.ecg_voltage = self.ecg_data_sliced[1]
        # print('ecg voltage')
        # print(self.ecg_voltage)

        return self.ecg_voltage

    def ecg_plot(self):
        """plots the ecg data in terms of time and voltage

        :param: time input from the ecg
        :param: voltage from the ecg
        :return: a plot of time vs. voltage
        """
        import matplotlib as mlp
        mlp.use('TkAgg')
        import matplotlib.pyplot as plt
        ecg_time = self.ecg_data[0]
        ecg_voltage = self.ecg_data[1]
        plt.figure(1)
        ecg_plot = plt.plot(ecg_time, ecg_voltage, 'b', label='ECG Original')
        #plt.figure(2)
        #peaks_plot = plt.plot(self.beats_time, self.ecg_voltage[:self.peaks], 'y', linewidth=5,
                              label='Peaks Detected')
        plt.xlabel('time')
        plt.ylabel('voltage')
        plt.show()
        return ecg_plot

    def find_voltage_extremes(self):
        """takes in the voltage data and returns the voltage extremes

        :param: takes ecg voltage array
        :return: ecg voltage min and max
        """
        import numpy as np
        full_voltage = self.ecg_data[1]
        max_voltage = np.max(full_voltage)
        # print('max voltage:', max_voltage)
        min_voltage = np.min(full_voltage)
        # print('min voltage:', min_voltage)
        self.voltage_extremes = (min_voltage, max_voltage)
        # print('voltage extremes:', self.voltage_extremes)
        return self.voltage_extremes

    def find_ecg_duration(self):
        """takes in ecg time and returns the duration

        :param: takes in ecg time
        :return: the duration
        """
        try:
            import numpy as np
            full_time = self.ecg_data[0]
            min_time = np.min(full_time)
            max_time = np.max(full_time)
            self.duration = max_time - min_time
        except TypeError:
            print('Data must be numbers')
        return self.duration

    @property
    def auto_correlate(self):
        """takes in ecg data and cross-correlates it with one ecg peak

        :param: takes in ecg data
        :return: cross correlation result
        """
        try:
            import numpy as np
            import matplotlib as mlp
            mlp.use('TkAgg')
            import matplotlib.pyplot as plt
            normalized_ecg_data = (self.ecg_data_sliced -
                                   np.min(self.ecg_data_sliced)) / (np.max(
                                    self.ecg_data_sliced) -
                                    np.min(self.ecg_data_sliced))

            ecg_kernel = normalized_ecg_data[0:330]
            self.correlation = np.correlate(normalized_ecg_data[1],
                                            ecg_kernel[1], 'full')
            print('correlation results:', self.correlation)

            correlation_plot = plt.plot(self.correlation)
            plt.xlabel('lag')
            plt.ylabel('correlation sum')
            plt.show()

            return self.correlation

        except ImportError:
            print('Unable to import required module')
        except TypeError:
            print('Unable to graph data, check data type')

    def find_peaks(self):
        """takes in cross correlation results and finds the peaks

        :param: cross correlation results
        :return: location of peaks
        """
        try:
            import numpy as np
            from scipy import signal
            self.peaks = signal.find_peaks_cwt(self.correlation, np.arange(1, 330))
            print('location of peaks:', self.peaks)
            return self.peaks
        except ValueError:
            print('Unable to detect peaks')

    def count_beats(self):
        """takes in the peaks and returns the number of peaks

        :param: peaks location
        :return: number of peaks
        """
        self.number_beats = len(self.peaks)
        print('number of beats detected:', self.number_beats)

        return self.number_beats

    def calculate_hr_bpm(self):
        """takes in number of beats and duration of ecg
        and returns mean heart rate

        :param: number of beats and duration of ecg
        :return: mean heart rate
        """
        import numpy as np
        end_time = np.max(self.ecg_time[0])
        print('end time', end_time)
        start_time = np.min(self.ecg_time[0])
        print('start time', start_time)
        time_elapsed = end_time - start_time
        self.meanHR = self.number_beats / (time_elapsed / 60)
        print('duration in seconds:', self.duration)
        print('mean HR (bpm):', self.meanHR)

        return self.meanHR

    def create_beats_array(self):
        """takes in peaks location and returns a beats time array

        :param: takes in peak location
        :return: beats time array
        """
        import numpy as np
        ecg_time = self.ecg_time[0]
        beats_time = ecg_time[self.peaks]
        self.beats_time = np.array(beats_time).tolist()
        print('beats time', self.beats_time)
        return self.beats_time

    def create_json(self):
        """creates a json file and writes returned values

        :param: test file, attributes of ECG class
        :return: json file with attributes of ECG class
        """
        import json
        from os.path import splitext
        import logging

        print(self.input_path)
        stem, _ = splitext(self.input_path)
        self.json_output = stem + '.json'
        print(self.json_output)

        logging.info('Info: Json file created')
        try:
            data = [{"voltage extremes": self.voltage_extremes},
                    {"ECG duration": self.duration},
                    {"Number of detected beats": self.number_beats},
                    {"mean HR in bpm": self.meanHR},
                    {'time of detected beats': self.beats_time}]
            with open(self.json_output, 'w') as jf:
                json.dump(data, jf)
            return self.json_output
        except ValueError:
            print('invalid json input')
            logging.debug('Error: json output')
            return None

    def main(self):
        """includes all the defined functions within the ecg class
        """
        import logging
        logging.info('Info: program started')

        self.ecg_data = self.read_data()
        self.ecg_time = self.read_time()
        self.ecg_voltage = self.read_voltage()
        self.voltage_extremes = self.find_voltage_extremes()
        self.duration = self.find_ecg_duration()
        ecg_plot = self.ecg_plot()
        self.correlation = self.auto_correlate
        self.peaks = self.find_peaks()
        self.number_beats = self.count_beats()
        self.meanHR = self.calculate_hr_bpm()
        self.beats_time = self.create_beats_array()
        #self.json_output = self.create_json()

        logging.info('Info: program ended')


if __name__ == "__main__":
    a = ECG('test_data1.csv', "./test_data/", 10)
