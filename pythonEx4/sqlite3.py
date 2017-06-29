import sqlite3
# cursor , execute all other on server
db = sqlite3.connect('db.sqlite')
c = db.cursor()
c.execute('insert into groups (st_name, g_name) values (?, ?)', ('Tom', 'AA-12'))

c.fetchone()
c.fetchmany(3)
c.fetchall()

c1 = c.execute('select * from students')
for row in c1:
	print(row)

db.commit()