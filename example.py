import pyhs2

conn = pyhs2.connect(host='localhost', 
					port=10000,
					authMechanism="PLAIN", 
					user='root', 
					password='test', 
					database='default')
cur = conn.cursor()
cur.execute("show tables")
for i in cur.fetch():
	print i
cur.close()
conn.close()
