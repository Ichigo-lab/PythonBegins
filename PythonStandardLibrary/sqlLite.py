import sqlite3
import json
from pathlib import Path

#movies = json.loads(Path("movies.json").read_text())
# print(movies)
# use db browser for sqlite
#conn = sqlite3.connect("mydb.sqlite3")

# with sqlite3.connect("mydb.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?,?,?)"  # ? is a placeholder
#     for movie in movies:
#         print(tuple(movie.values()))
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

with sqlite3.connect("mydb.sqlite3") as conn:
    command = "SELECT * from Movies"  # ? is a placeholder
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
