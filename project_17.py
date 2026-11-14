import argparse
import os
import re

parser = argparse.ArgumentParser()

parser.add_argument('path')
parser.add_argument('--text')

args = parser.parse_args()


def analyze_file(file_path):
    logs = []
    current_log = ''
    file_name = os.path.basename(file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        for all_read in file:

            if re.match(r'\d{4}-\d{2}-\d{2}', all_read):
                if current_log:
                    logs.append((file_name, current_log))

                current_log = ''

            current_log += all_read

        if current_log:
            logs.append((file_name, current_log))

    for file_name, log in logs:
        if args.text in log:
            words = log.split()

            for index, word in enumerate(words):
                if args.text in word:
                    error_index = index
                    snippet = words[max(0, error_index - 5):error_index + 6]
                    print(' '.join(snippet))
                    print(file_name)
                    print(log[:23])


if not args.text:
    print('Не указан текст для поиска')

elif os.path.isdir(args.path):
    files = os.listdir(args.path)

    if not files:
        print('Папка пустая')

    else:
        for all_file in files:
            file_path = os.path.join(args.path, all_file)
            analyze_file(file_path)

elif os.path.isfile(args.path):
    analyze_file(args.path)

else:
    print('Файл или папка не найдены')


