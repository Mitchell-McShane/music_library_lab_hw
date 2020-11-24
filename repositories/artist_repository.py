from models.artist import Artist
from models.album import Album

from db.run_sql import run_sql

#Create
def save(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING id"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['artist_name'], row['id'])
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['artist_name'], result['id'])
    return artist

def update(artist):
    sql = "UPDATE artists SET (artist_name) = (%s) WHERE is = %s"
    values = [artist.artist_name, artist.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM artists"
    run_sql(sql)