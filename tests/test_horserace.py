from unittest import TestCase
from horserace.horserace import Step


class TestStep(TestCase):

    def test_step_init(self):
        step = Step()
        actual = step.current()
        expected = 0
        self.assertEqual(actual, expected)