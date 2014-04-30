import datetime
import itertools
import sqlite3

import dateutil.parser
import pytz

"""Dates and times in sqlite3 are stored as TEXT, REAL, or INTEGER values

TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").
REAL as Julian day numbers, the number of days since noon in Greenwich on November 24, 4714 B.C. according to the proleptic Gregorian calendar.
INTEGER as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC.

"""

def adapt_datetime(dt):
    return dt.isoformat().replace('+','-')
def convert_datetime(ts):
    return dateutil.parser.parse(ts)

sqlite3.register_adapter(datetime.datetime, adapt_datetime)
sqlite3.register_converter('timestamp', convert_datetime)

input_values = []

input_values.append([datetime.datetime(2019,11,1,12,0, tzinfo=pytz.UTC)])

us_pacific_tz = pytz.timezone('US/Pacific')
input_values.append([datetime.datetime(2019,11,1, tzinfo=us_pacific_tz)])

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
