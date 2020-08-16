import json
from pathlib import Path


# create json file
# movies = [
#     {"id": 1, "title": "Ironman", "year": 2008},
#     {"id": 2, "title": "Thor", "year": 2011},
#     {"id": 3, "title": "Avengers", "year": 2012},
# ]

# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0]["title"])
