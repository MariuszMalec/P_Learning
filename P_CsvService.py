import os
import sys, csv
import P_Logger

class CsvManager:
    __allValues = []
    __fileName = ""
    
    def __init__(self):
        self.__allValues = []
        self.__fileName = ""
        
    def setFileName(self, fileName):
        self.__fileName = fileName        
        
    def load(self):
        self.__allValues = []
        with open(self.__fileName, newline='') as f:
            reader = csv.DictReader(f)
            try:
                for row in reader:
                    self.__allValues.append(row['Name'] + "," + row['Value'])
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(self.__fileName, reader.line_num, e))

    def hasVar(self, name):
        getName = lambda string : string.split(',')[0]
        getValue = lambda string : string.split(',')[1]
        value = "-"
        for item in self.__allValues:
            if getName(item) == name:
                value = getValue(item)
                return True
        if value == "-":
            P_Logger.logger.error(str(name) + " not found in csv")
        return False
                
    def getVar(self, name):
        getName = lambda string : string.split(',')[0]
        getValue = lambda string : string.split(',')[1]
        value = "-"
        for item in self.__allValues:
            if getName(item) == name:
                value = getValue(item)
        return value
    
def main():    
    folder = r'./Source'
    if not (os.path.dirname(folder)):
            P_Logger.logger.error('brak katalogu!')
            sys.exit()
    file = os.path.join(folder, "LADT1100P1002.csv")    
    service = CsvManager()
    service.setFileName(file)
    service.load()
    dn = service.getVar("DN")
    P_Logger.logger.info("DN = " + dn)
        

if __name__ == '__main__':
    main()    
