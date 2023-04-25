import unittest
from models.artist import Artist


class TestArtist(unittest.TestCase):

    def setUp(self):
        self.album = Artist("Berry Berry")

    def test_album_has_name(self):
        self.assertEqual("Berry Berry", self.album.name)
