import pyhs2

conn = pyhs2.connect(host='192.168.100.139', 
					port=20000,
					authMechanism="PLAIN", 
					user='hdfs', 
					password='test', 
					database='default')


cur = conn.cursor()


cur.execute("SELECT * FROM hs2")

for i in cur.fetch():#
	print i

#print len(cur.fetch())

cur.close()
conn.close()

