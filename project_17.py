import argparse
import os
path = r'D:\змея\qwerty-qa-main\data\logs'

parser = argparse.ArgumentParser()

parser.add_argument('path')
parser.add_argument('--text')

args = parser.parse_args()

if os.path.isdir(path):
    open(path)
elif os.path.isfile(path):
    open('file')
else:
    print('файл или папка пуста')











