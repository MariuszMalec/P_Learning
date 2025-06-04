import os
import P_Logger
import csv
from prettytable import PrettyTable
from csv import DictReader, DictWriter

class ReaderCsvFile:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def ReadCsvAsFileHandler(self):
        try:
            with open(self.input_file, mode='r', newline='') as file_handler:
                header = file_handler.readline()
                P_Logger.logger.info(header.strip())

                for line in file_handler:
                    P_Logger.logger.info(line.strip())

        except Exception as e:
            P_Logger.logger.error(" " + str(e))

    def ReadCsvAsPrettyTable(self):
        try:
            with open(self.input_file, mode='r', newline='') as file_handler:
                table = PrettyTable()
                header = file_handler.readline()
                table.field_names = header.strip().split(',')

                for line in file_handler:
                    table.add_row(line.strip().split(','))

                print(table)

        except Exception as e:
            P_Logger.logger.error(" " + str(e))         

    def AddRowToFile(self):
        try:
            with open(self.input_file, mode='a+', newline='') as file_handler:
                new_row = ['3000','','test', 'true', 'MilliMeter','','Bool','','','','','','\n']
                file_handler.write(','.join(new_row))

        except Exception as e:
            P_Logger.logger.error(" " + str(e))                  

    def ReadCsvAsDict(self):
        try:
            with open(self.input_file, mode='a+', newline='') as file_handler:
                file_handler.seek(0)
                reader = DictReader(file_handler)
                P_Logger.logger.info(reader.fieldnames)

                for row in reader:
                    P_Logger.logger.info(row)

        except Exception as e:
            P_Logger.logger.error(" " + str(e))                  

    def WriteCsvAsDict(self):
        try:
            with open(self.input_file, mode='r', newline='') as file_handler , \
                open(self.output_file, mode='a+', newline='') as output_file:
                file_handler.seek(0)
                reader = DictReader(file_handler)
                writer = DictWriter(output_file, fieldnames=reader.fieldnames)
                for row in reader:
                    writer.writerow(row)

        except Exception as e:
            P_Logger.logger.error(" " + str(e))               

    def FixCountCsvAsDict(self):
        try:
            with open(self.input_file, mode='r', newline='') as file_handler , \
                open(self.output_file, mode='w', newline='') as output_file:
                file_handler.seek(0)
                reader = DictReader(file_handler)
                writer = DictWriter(output_file, fieldnames=reader.fieldnames)
                for n, row in enumerate(reader):
                    row['Id'] = n+1
                    writer.writerow(row)

        except Exception as e:
            P_Logger.logger.error(" " + str(e))                           

def main():
    P_Logger.logger.info("How to read csv file")
    myDir = r'C:/Users/user/source/repos/P_Learning/Source'

    # Path to the original CSV file
    input_file = os.path.join(myDir, "LADT1100P1002.csv")

    # Path to the new CSV file to save the data
    output_file = os.path.join(myDir, "LADT1100P1002_copy.csv")

    reader = ReaderCsvFile(input_file, output_file)

    #reader.ReadCsvAsFileHandler()

    #reader.AddRowToFile()

    #reader.ReadCsvAsPrettyTable()

    #reader.ReadCsvAsDict()

    #reader.WriteCsvAsDict()

    reader.FixCountCsvAsDict()

if __name__ == '__main__':
    main()        

