Author : Surender Kumar
Contact: kumarsu44@gmail.com

A Train Scheduler
=================
Given are two files containing real-world data of Indian Railways.
Stations.txt
Stations.txt contains the codes and names of some of the important stations in India. Each line
contains a station code and the station name separated by the delimiter ‘|’ (pipe), in the following format:

station code|station name
Note that the station name can contain multiple words separated by blanks, but the station code does
not contain blanks.
Example lines from Stations.txt:
AA|ATARIA
KGP|KHARAGPUR
HWH|HOWRAH
CSTM|MUMBAI CST
TrainSchedules.txt
TrainSchedules.txt contains the schedule of some of the express trains in Indian Railways.
Each line contains the schedule of a single train in the following format: (fields separated by delimiter ‘|’)

train code|dayX|timeX|stationX|dayY|timeY|stationY|...
Here ‘train code’ is the code of the train, ‘stationX’ and so on are the codes of the stations at which
the train stops, and the train reaches station stationX at time timeX on day dayX. Day 1 implies the
same day on which the train began its journey, day 2 implies the next day, and so on. The times are
given in 24-hour hh:mm format.
Example lines from TrainSchedules.txt:
2021|1|06:20|HWH|1|07:58|KGP|1|09:42|TATA|1|10:51|CBSA|1|11:41|DPS|
1|11:57|NOMD|1|12:24|BJMD|1|13:15|BBN
2345|1|15:50|HWH|1|17:07|BWN|1|17:55|BHP|1|18:57|RPH|1|21:45|MLDT|
1|23:50|KNE|2|01:50|NJP|2|04:03|NCB|2|04:23|NOQ|2|06:25|NBQ

Part 1
Write a Python script that reads the above two files and stores the data in the following tables in a
MySQL database. The host, username, password and database name are to be taken as command line
arguments. The Python script for this part should be named ct2_1.py
Table to store the schedule of trains and stations in the following tables.
trainschedule (traincode, stncode, day, time)
station (stncode, stnname)
The tables have to be created using the Python program itself. Note that the names of the tables and
the columns must be exactly as written above (all small case letters).
Example usage: python ct2_1.py 127.0.0.1 user1 pass1 db1 fills in the data parsed
from the files Stations.txt and TrainSchedules.txt into the above mentioned tables, in the database
‘db1’ in host ‘127.0.0.1’, to be accessed with username ‘user1’ and password ‘pass1’.

Part 2
Write a Python script that accepts the name of a station as a command-line argument and displays the
names of all stations that can be reached from the given station via a direct train. The Python script
should be named ct2_2.py
Example Usage: python ct2_2.py HOWRAH displays names of all stations which can be reached
from Howrah via a direct train.

Part 3
Write a Python script that accepts the names of two stations (say, X and Y) as command-line arguments,
and displays the codes of the direct trains that can be used to travel from X to Y. The Python
script should be named ct2_3.py
Example Usage: python ct2_3.py HOWRAH KHARAGPUR displays the trains that can be used
to travel from Howrah to Kharagpur.

Part 4
Write a Python script that accepts the names of two stations (say, X and Y) and a time T as commandline
arguments, and displays the codes of the trains that can be used to reach Y from X before time T
on some day (i.e. only those trains should be listed which reach Y at or before time T). Before means
within six hours of the given time. For example before 12:00 hrs means in the time period 06:00 hrs
to 12:00 hrs (both inclusive). Also before 01:00 hrs means in the time period of 19:00 hrs to 01:00
hrs (both inclusive). T will be given in 24-hour hh:mm format. The Python script should be named
ct2_4.py
Example Usage: python ct2_4.py HOWRAH KHARAGPUR 11:30 displays the trains that can
be used to travel from Howrah to Kharagpur, so that one reaches Kharagpur in the interval 05:30 hrs
to 11:30 hrs.

Part 5
Write a Python script that accepts the name of a station X and a time T as command-line arguments,
and displays the code of the trains which reach station X before time T from any station. The definition
of before is same as with part 4. The Python script should be named ct2_5.py
Example Usage: python ct2_5.py HOWRAH 14:30 displays the trains that reach Howrah at
or before 14:30 hrs.

Part 6
Write a Python script that accepts the name of a station X as a command-line argument, and displays
the busiest hour at station X, i.e. that hour during which the maximum number of trains reach station
X. The Python script should be named ct2_6.py
Example Usage: python ct2_6.py KHARAGPUR displays the hour during which the maximum
number of trains reach Kharagpur. The hour can be displayed in the format 14:00–15:00.