import csv
# Saves fatigue recognition records in the file records.cvs
def recorder(date,label= 'unknown'):
    with open('records.csv', 'a') as f:

        f.writelines(f'\n Event: {label},{date}')