import csv
import time

with open('mendrisio-chiasso-immobiliari.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Start the script')
            line_count += 1
        else:
            print(row[0])
            print(line_count)
            line_count += 1
    print('Processed {line_count} lines.')




