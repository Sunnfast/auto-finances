import csv
from unicodedata import category
import gspread
import time


MONTH = 'April' #change this for month to run; will go to tab with same name

# file = f"[bank's name redacted]_{MONTH}.csv"

transactions = []

# def [redacted](file):

        with open(file, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                        date = row[0]
                        name = row[1]
                        amount = row[2]
                        category = ''
                        # categories below redacated to protect personal information
                        #if name == [redacted]:
                                # category = '[redacted]'
                        # if name == [redacted]:
                                # category = '[redacted]'
                        # if name == [redacted]:
                                # category = '[redacted]'
                        # if name == [redacted]:
                                # category = '[redacted]'
                        #if amount == [redacted]:
                                # category ='[redacted]'
                        transaction = ((date, name, amount, category))
                        
                        transactions.append(transaction)
                return transactions

                
sa = gspread.service_account()
sh = sa.open("Personal Finances 2022")

wks = sh.worksheet(f"{MONTH}")

# rows = [redacted](file)

for row in rows:
        wks.insert_row([row[0], row[1], row[3], row[2]], 3)
        time.sleep(1.5)

