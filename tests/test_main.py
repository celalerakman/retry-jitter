import unittest
import main as m

class Behavior(unittest.TestCase):
    def test_behavior(self):
        import random
        for attempt in range(20): self.assertTrue(0<=m.delay(attempt,random.Random(1))<=300)
        with self.assertRaises(ValueError): m.delay(-1)
