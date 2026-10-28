import json
from sys import orig_argv


def read_file(filename):
    file_data = open(filename, 'r')
    # data = file_data.read()
    data = json.load(file_data)
    file_data.close()
    print(data)
    return data

data1 = read_file(r'D:\змея\учеба\data1.txt.txt')
data2 = read_file(r'D:\змея\учеба\data2.txt.txt')

print(data1['Country'])
print(data2['Country'])
print(data2['avg_temp'])
print(data1['avg_temp'])





class CountryData(object):

    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_file()
        self.country = self.data['Country']
        self.__avg_temp = self.data['avg_temp']
        self.comfort  = self.is_comfort()


    def read_file(self):
        file_data = open(self.filename, 'r')
        data = json.load(file_data)
        file_data.close()
        print(data)
        return data


    def is_comfort(self):
        return self.__avg_temp > 25



    def __str__(self):
       return f'File {self.filename} with data {self.data}'



    def __repr__(self):
       return f'File {self.filename} with data {self.data}'



    def __lt__(self, other):
        return self.__avg_temp  < other.__avg_temp


    def __le__(self, other):
        return self.__avg_temp  <= other.__avg_temp


    def __add__(self, other):
        return self.data , other.data




class CountryDataMin(CountryData):

    def __init__(self, filename):
        super().__init__(filename)
        self.min_temp = self.data['min_temp']





dataa1 = CountryData(r'D:\змея\учеба\data1.txt.txt')
print(dataa1.country)

dataa2 = CountryData(r'D:\змея\учеба\data2.txt.txt')
dataa3 = CountryDataMin(r'D:\змея\учеба\data3.txt.txt')

dataa1.avg_temp = 24234
print(dataa1.avg_temp)
print(dataa3.min_temp)

print(dataa1)
print(dataa1 < dataa3)
print(dataa1 <= dataa3)
print(dataa1 > dataa3)
print(dataa1 >= dataa3)
print(dataa1 + dataa3)