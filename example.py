import pyhs2

conn = pyhs2.connect(host='192.168.100.139', 
					port=20000,
					authMechanism="PLAIN", 
					user='hdfs', 
					password='test', 
					database='default')

conn.close()

'''
cur = conn.cursor()

cur.execute("SELECT Host,User FROM user")

print(cur.description)

print()

for row in cur:
   print(row)

cur.close()
conn.close()
'''