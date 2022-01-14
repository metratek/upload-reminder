import os.path
from datetime import date
import datetime
import time
import sys
from sendmail import sendmail
import shutil

sleep_secs = 5

sql_recipients = ['gasparem@moh.gr', 'sourlist@moh.gr', 'info@metratek.co.uk']
intl_recipients = ['dchrissafis@moh.gr', 'info@metratek.co.uk']

# SQLite settings
sql_filename = 'Optisched.db'
sql_dir = 'C:\\DATA\\Schedulers\\'
sql_hour = 11
sql_stop_loop = False

# Intl settings
intl_dir = 'C:\\DATA\\Planners\\'
intl_hour = 14
intl_stop_loop = False

prev_date = date.today()

while True:
    today = date.today()
    now = datetime.datetime.now()

    if today != prev_date:
        print("Day change")
        sql_stop_loop = False
        intl_stop_loop = False

    if not sql_stop_loop:
        sql_found = os.path.isfile(sql_dir + sql_filename)
        if sql_found:
            sendmail(sql_recipients, "File " + sql_filename + " uploaded - Thanks")
            sql_stop_loop = True
        elif now.hour == sql_hour:
            sendmail(sql_recipients, "Reminder: Please upload file " + sql_filename + " - Disregard if on holiday")
            sql_stop_loop = True

    if not intl_stop_loop:
        suffix = today.strftime("_%d_%m_%y.xlsx")
        intl_filename = 'input' + suffix
        intl_found = os.path.isfile(intl_dir + intl_filename)

        if intl_found:
            sendmail(intl_recipients, "File " + intl_filename + " uploaded - Thanks")
            new_path = shutil.move(intl_filename, os.path.abspath(
                os.path.join(os.path.dirname(intl_filename), f'../Spreadsheets')))
            intl_stop_loop = True
        elif now.hour == intl_hour:
            sendmail(intl_recipients, "Reminder: Please upload file " + intl_filename + " - Disregard if on holiday")
            intl_stop_loop = True

    prev_date = date.today()
    print(f'Waiting for {sleep_secs}secs at {datetime.datetime.now()}')
    time.sleep(sleep_secs)  # wait 1 min
