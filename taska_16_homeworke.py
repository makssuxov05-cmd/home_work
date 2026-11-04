import requests
import csv
import io


url = 'https://raw.githubusercontent.com/eugene-okulik/qwerty-qa/main/homework/eugene_okulik/Lesson_16/hw_data/data.csv'

response = requests.get(url)
response.raise_for_status()

virtual_file = io.StringIO(response.text)
file_data = csv.reader(virtual_file)

for row in file_data:
    print(row)