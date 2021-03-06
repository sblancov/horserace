from unittest import TestCase
from unittest.mock import Mock
from horserace.models.race import Horse
from horserace.models.speed import RandomSpeed


class TestHorse(TestCase):

    def setUp(self):
        speed = Mock()
        speed.next.return_value = 1
        self.horse = Horse('horse', speed)

    def test_run(self):
        self.horse.run()
        actual = self.horse.locate()
        expected = 1
        self.assertEqual(actual, expected)

    def test_has_not_arrive(self):
        finish = 1
        actual = self.horse.has_arrive(finish)
        self.assertFalse(actual)

    def test_has_arrive(self):
        finish = 0
        actual = self.horse.has_arrive(finish)
        self.assertTrue(actual)


class TestRandomSpeed(TestCase):

    def test_next(self):
        speed = RandomSpeed()
        actual = speed.next()
        expected = actual == 0 or actual == 1
        self.assertTrue(expected)
