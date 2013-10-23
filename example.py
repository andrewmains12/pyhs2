import pyhs2

conn = pyhs2.connect(host='localhost', 
					port=10000,
					authMechanism="PLAIN", 
					user='root', 
					password='test', 
					database='default')


cur = conn.cursor()


cur.execute("SELECT * FROM hs2")

for i in cur.fetch():#
	print i

#print len(cur.fetch())

cur.close()
conn.close()

