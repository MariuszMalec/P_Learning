import os
import sys
import unittest

from P_CsvService import CsvService


def init_service():
    folder = r'./Source'
    if not (os.path.dirname(folder)):
        sys.exit()
    file = os.path.join(folder, "LADT1100P1002.csv")
    service = CsvService()
    service.setFileName(file)
    service.load()
    return service


class test_P_CsvService(unittest.TestCase):

    def setUp(self):
        self.service = init_service()

    def test_hasVar_WhenFound_ReturnTrue(self):
        result = self.service.hasVar("DN")
        self.assertEqual(result, True)

    def test_hasVar_WhenNotFound_ReturnFalse(self):
        result = self.service.hasVar("test")
        self.assertEqual(result, False)

    def test_getVar_WhenFound_ReturnValue(self):
        result = self.service.getVar("DN")
        self.assertEqual(result, "559.7")


if __name__ == '__main__':
    unittest.main()
