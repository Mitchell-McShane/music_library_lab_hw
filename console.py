import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


album_repository.delete_all()
artist_repository.delete_all()


artist_1 = Artist('Nada Surf')
artist_repository.save(artist_1)

album_1 = Album("You Know Who You Are", artist_1, "Rock")
album_repository.save(album_1)
album_2 = Album("Never Not Together", artist_1, "Rock")
album_repository.save(album_2)

for album in album_repository.select_all():
    print(album.__dict__)

pdb.set_trace()