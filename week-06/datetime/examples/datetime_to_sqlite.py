import datetime
import sqlite3

import pytz

# def adapt_datetime(ts):
    # return time.mktime(ts.timetuple())

# sqlite3.register_adapter(datetime.datetime, adapt_datetime)


# t1=datetime.datetime(2019,11,1,12,0, tzinfo=pytz.UTC)

us_pacific_tz = pytz.timezone('US/Pacific')
# t2 = datetime.datetime(2019,11,1, tzinfo=us_pacific_tz)
t1 = datetime.datetime.now()
t2 = datetime.datetime.now()

conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
# conn = sqlite3.connect(":memory:")

cursor = conn.cursor()

cursor.execute("CREATE TABLE timetable(t timestamp)")

cursor.executemany("INSERT INTO timetable(t) VALUES (?)", ([t1],[t2]))

for row in cursor.execute("SELECT t FROM timetable"):
    t = row[0] 
    print t
    print type(t)
