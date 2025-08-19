import sqlite3

conn = sqlite3.connect('emaildb.db')
curn = conn.cursor()

curn.execute('''DROP TABLE IF EXISTS counts''')
curn.execute('''CREATE TABLE counts (email TXT,count INTEGER)''')

fname= input('Enter file name:')
if len(fname) < 1 : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    curn.execute('SELECT count FROM counts WHERE email = ? ',(email,))
    row = curn.fetchone()
    if row is None:
        curn.execute('''INSERT INTO counts (email,count) VALUES (?,1)''',(email,))
    else:
        curn.execute('UPDATE counts SET count = count + 1 WHERE email = ?',(email,))
    conn.commit()

sqlstr='SELECT email,count FROM counts ORDER BY count DESC LIMIT 10'
for row in curn.execute(sqlstr):
    print(str(row[0]),row[1])
