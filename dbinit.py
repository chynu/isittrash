import sqlite3

db = sqlite3.connect('mydb.db')

cursor = db.cursor()
cursor.execute('''DROP TABLE trash''')
cursor.execute('''
    CREATE TABLE trash(name TEXT unique, disposal TEXT,
    category TEXT, url TEXT, synonymns TEXT) 
''')

cursor.execute("INSERT INTO trash VALUES('apple', 'throw in compost', 'compost', 'http://www.spyderonlines.com/images/wallpapers/apple-image/apple-image-16.jpg', '[fruit gala]')")

db.commit()
cursor.execute("SELECT * FROM trash")
for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0}, {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2], row[3], row[4]))
db.close()
