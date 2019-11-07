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

sfile=open('Stations.txt')
tfile=open('TrainSchedules.txt')

stnlines=sfile.readlines()
trainlines=tfile.readlines()

################### part1 ########################################################################
for sl in stnlines:
	stnpairs=sl.split('|')
	insertstn="INSERT INTO station VALUES("+"'"+stnpairs[0]+"'"+", "+"'"+stnpairs[1]+"'"+");"
	print "Inserted into station: ", stnpairs[0], stnpairs[1]
	cursor.execute (insertstn)
	cursor.execute ("commit")

for tl in trainlines:
	trainatt=tl.split('|')
	tlen=len(trainatt)
	i=1
	j=2
	k=3
	while k<=tlen-1:
		print trainatt[i], trainatt[j], trainatt[k]
		inserttrain="INSERT INTO trainschedule VALUES("+ "'"+trainatt[0]+"'" + "," + "'"+trainatt[k]+"'" + "," + "'"+trainatt[i]+"'" + "," + "'"+trainatt[j]+"'" +");"
		cursor.execute (inserttrain)
        	cursor.execute ("commit")
		i=i+3
		j=j+3
		k=k+3



