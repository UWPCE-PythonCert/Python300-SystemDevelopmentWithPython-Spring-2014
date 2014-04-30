import datetime
import itertools
import sqlite3

import pytz

"""Dates and times in sqlite3 are stored as TEXT, REAL, or INTEGER values

TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").
REAL as Julian day numbers, the number of days since noon in Greenwich on November 24, 4714 B.C. according to the proleptic Gregorian calendar.
INTEGER as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC.

sqlite3 will handle the translation from datetime to strings
"""

input_values = []

input_values.append([datetime.datetime(2019,11,1,12,0)])
input_values.append([datetime.datetime(2019,11,1,13,0)])
# input_values.append([datetime.datetime(2019,11,1,12,0,tzinfo=pytz.UTC)])

conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)

cursor = conn.cursor()

cursor.execute("CREATE TABLE timetable(t timestamp)")

cursor.executemany("INSERT INTO timetable(t) VALUES (?)", input_values)

for row,input_value in itertools.izip(cursor.execute("SELECT t FROM timetable"), input_values):
    from_db = row[0] 
    from_input = input_value[0]
    print from_db
    print type(from_db)
    print from_input
    assert(from_db == from_input)
