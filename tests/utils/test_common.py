from unittest import TestCase
from horserace.utils.common import Step


class TestStep(TestCase):

    def test_step_init(self):
        step = Step()
        actual = step.current()
        expected = 0
        self.assertEqual(actual, expected)

    def test_step_inc(self):
        step = Step()
        step.inc()
        actual = step.current()
        expected = 1
        self.assertEqual(actual, expected)
