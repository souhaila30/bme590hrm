class Read_ecg():

    """

    Reads ECG files and obtain information from there

    """

    def __init__(self, fileType, relativePath):

        """

        Initializes the attributes of Read_ecg

        """

        self.relativePath = relativePath
        self.fileType = fileType

    import logging
    logging.basicConfig(filename = 'logging.txt', format = '%(asctime)s %(message)s', datefmt
                            ='%m/%d/%Y & I:%M:%S %p', level = logging.DEBUG)

    def collect_files(self):

        """

        collects all files of the appropriate file type

        :param filetype: type of file to be imported
        :return imported_files: all files found of the file type needed

        """

        fileType = '*.csv'
        relativePath = "./test_data/"
        import os
        inputFilesPath = os.path.join(relativePath, fileType)
#self.relativePath, self.fileType

        import glob
        imported_files = glob.glob(inputFilesPath)
        print(imported_files)
        return imported_files

    def read_files(imported_files):
        import pandas as pd
        for imported_file in imported_files:
            ecg_data = pd.read_csv(imported_file, delimiter = ',', header = None)
            for row in ecg_data:
                ecg_time = row[1]
            for row in ecg_data:
                ecg_voltage = row[2]

            return ecg_time, ecg_voltage






