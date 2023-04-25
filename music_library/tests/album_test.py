import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        self.album = Album("Summer Jams", "Blues", "Berry Berry")
    
    def test_album_has_title(self):
        self.assertEqual("Summer Jams", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("Blues", self.album.genre)
    
    def test_album_has_artist(self):
        self.assertEqual("Berry Berry", self.album.artist)