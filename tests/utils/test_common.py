from unittest import TestCase
from horserace.utils.common import StepCounter


class TestStep(TestCase):

    def setUp(self):
        self.step = StepCounter()

    def test_step_init(self):
        actual = self.step.current()
        expected = 0
        self.assertEqual(actual, expected)

    def test_step_inc(self):
        self.step.inc()
        actual = self.step.current()
        expected = 1
        self.assertEqual(actual, expected)
