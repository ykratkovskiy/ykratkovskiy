from unittest import TestCase, result
from test1 import dot_product


class DotProductTestCase(TestCase):
    def test_onevalues(self):
        result = dot_product([1],[2])
        self.assertEqual (result,6)


def test_inconsistent(self):
    result = dot_product([1],[4,5])
