from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

## Create and save artists:
artist1 = Artist("Leos")
artist_repository.save(artist1)
artist2 = Artist("Stars")
artist_repository.save(artist2)


## Create and save albums:
album1 = Album("The Best Of", "Alternative", artist1)
album_repository.save(album1)
album2 = Album("The Worst Hits", "Alternative", artist2)
album_repository.save(album2)

## Delete all Artists / Albums : 
# album_repository.delete_all()
# artist_repository.delete_all()

## Delete where id matches
# album_repository.delete(5)
# artist_repository.delete(7)

## Find Artists/Albums by their ID (select)
# result = album_repository.select(11)
# print(result.__dict__)

## To update an Artist/Album
# album1.title = "The Best Hits"
# album_repository.update(album1) 
## not working ...
# album1.title = "The Best Hits"
# album_repository.update(album1) 
## still not working ...
album2 = Album("The Best Hits", "Alternative", artist2)
album_repository.update(album2)
## still not working ...

## List all Artists/Albums (select_all)
albums = album_repository.select_all()
for album in albums:
    print(album.__dict__)

