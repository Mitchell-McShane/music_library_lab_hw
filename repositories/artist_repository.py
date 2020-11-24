from models.artist import Artist
from models.album import Album

from db.run_sql import run_sql

#Create
def save(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING id"
    values = [artist.artist_name]
    # print(values)
    results = run_sql(sql, values)
    # print(results)
    id = results[0]['id']
    artist.id = id
    return artist