import sqlite3
from Account import Account

conn = sqlite3.connect('data/sql.db')

cursor = conn.cursor()

# cursor.execute("""CREATE TABLE account(  
#                 ID integer,
#                 name text,
#                 username text
#                )""")

user1 = Account(name="Ali",username="amaamoun")

cursor.execute("INSERT INTO account VALUES (?, ?, ?)", 
               (user1.getID(), user1.get_name(), user1.get_username()))

cursor.execute("""INSERT INTO account VALUES(:ID,:name,:username), 
               {'ID' : account.ID, 'name' : account.name, 'username' : account.username}""")

cursor.execute("""SELECT * FROM account WHERE name='Ridham'""")

print(cursor.fetchone())

conn.commit()

conn.close()

#res = cursor.execute("SELECT name FROM sqlite_master")