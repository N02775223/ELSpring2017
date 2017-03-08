import os
import time
import sqlite3 as mydb
import sys
import datetime
#Author@ Jason Goodman
def logTime():
    xdate = time.strftime('%Y-%m-%d') #Year-Month-Day, ex: '2017-03-08'
    xtime = time.strftime('%H-%M-%S') #Hour-Minute-Second, ex: '18-59-17'
    return [xdate, xtime]
#print readTime()

