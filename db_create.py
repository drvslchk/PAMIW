import sqlite3

db_lp = sqlite3.connect('username_password.db')
cursor_db = db_lp.cursor()
sql_create = '''CREATE TABLE IF NOT EXISTS passwords( 
username TEXT PRIMARY KEY,
password STRING NOT NULL);'''

cursor_db.execute(sql_create)
db_lp.commit()

cursor_db.close()
db_lp.close()
