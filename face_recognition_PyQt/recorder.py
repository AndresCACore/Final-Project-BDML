import csv

def recorder(date,label= 'unknown'):
    with open('records.csv', 'a') as f:

        f.writelines(f'\n Event: {label},{date}')