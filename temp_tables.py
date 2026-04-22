import sqlite3
conn = sqlite3.connect('data/01_raw/database.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [row[0] for row in cursor.fetchall()]
print('\n'.join(tables))
conn.close()