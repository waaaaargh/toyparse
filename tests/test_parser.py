from unittest import TestCase

from toyparse.parser import Parser

class TestParser(TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_describe(self):
        self.assertIn("Parser", self.parser.describe()['name'])
