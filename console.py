import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


nada_surf = Artist('Nada Surf')
artist_repository.save(nada_surf)

pdb.set_trace()