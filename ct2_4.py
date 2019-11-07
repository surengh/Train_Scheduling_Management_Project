# Author : Surender Kumar
# Contact: kumarsu44@gmail.com

import MySQLdb
import sys
import Queue

#host=raw_input('Enter host: ')
#username=raw_input('Enter Username: ')
#password=raw_input('Enter passwd: ')
#database=raw_input('Enter database: ')

#conn=MySQLdb.connect(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
#conn=MySQLdb.connect(host, username, password, database)
conn=MySQLdb.connect("localhost", "labtest", "labtest12", "labtest")
cursor = conn.cursor ()


################### part3 ########################################################################
## Fetching stncode for given stnname first ##
TSCQ="select distinct stncode from station where stnname like "+ '"%'+str(sys.argv[1])+'%"'+";"
#TCQ="select * from station;"
cursor.execute(TSCQ)
stnCode=cursor.fetchone()
stnCode="%s" %stnCode
print stnCode

## Lets find all traincode of train which pass from above stnCode ##
TCQ="select distinct traincode from trainschedule where stncode="+ '"'+stnCode+'"'+";"
cursor.execute(TCQ)
trainRows=cursor.fetchall()
trainList=[]
for row in trainRows:
	tr="%s" %row
	trainList.append(str(tr))

## Find list of stnname which can be reached via each of above train ##
print "From station: ", stnCode, "following are trains and their reachable stations list"
for itrain in trainList:
	TSQ="select distinct stncode from trainschedule where traincode="+ '"'+itrain+'"' + "and atime<="+sys.argv[3]+";"
	cursor.execute(TSQ)
	stnRows=cursor.fetchall()
	for sow in stnRows:
        	sr="%s" %sow
        	istnList.append(str(sr))
	if str(sys.argv[2]) in istnList:
		print "Train Code: ", itrain





