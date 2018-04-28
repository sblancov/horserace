from unittest import TestCase, skip
from horserace.utils.config import FileLoader


@skip
class TestFileLoader(TestCase):

    def setUp(self):
        self.loader = FileLoader()

    def test_default_distance(self):
        actual = self.loader.distance()
        expected = 8
        self.assertEqual(actual, expected)
