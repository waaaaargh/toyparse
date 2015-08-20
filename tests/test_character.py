from unittest import TestCase

from toyparse.character import CharacterParser, NotCharacterParser
from toyparse.parser import ParseError, EndOfString

class TestCharacterParser(TestCase):
    def setUp(self):
        self.cparse = CharacterParser("c")

    def test_accept(self):
        self.assertEqual(
            self.cparse.parse("c"),
            ("c", "")
        )

        self.assertEqual(
            self.cparse.parse("cool"),
            ("c", "ool")
        )

    def test_fail(self):
        self.assertRaises(ParseError, self.cparse.parse, "f")
        self.assertRaises(EndOfString, self.cparse.parse, "")


class TestNotCharacterParser(TestCase):
    def setUp(self):
        self.ncparse = NotCharacterParser("c")

    def test_accept(self):
        self.assertEqual(
            self.ncparse.parse("f"),
            ("f", "")
        )
        self.assertEqual(
            self.ncparse.parse("foo"),
            ("f", "oo")
        )

    def test_fail(self):
        self.assertRaises(ParseError, self.ncparse.parse, "c")
        self.assertRaises(EndOfString, self.ncparse.parse, "")

