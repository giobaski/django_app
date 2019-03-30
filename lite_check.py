import sqlite3
conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

c.execute("""
        SELECT * FROM music_album
            """)
print(c.fetchall())

c.execute("""
        SELECT * FROM music_song
            """)

print(c.fetchall())