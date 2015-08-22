from unittest import TestCase

from toyparse.character import *
from toyparse.parser import ParseError
from toyparse.combinator import SequenceParser

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


class TestCharacterClassParser(TestCase):
    def setUp(self):
        self.ccparser = CharacterClassParser("abc")

    def test_accept(self):
        self.assertEqual(
            self.ccparser.parse("a"),
            ("a", "")
        )
        self.assertEqual(
            self.ccparser.parse("b"),
            ("b", "")
        )
        self.assertEqual(
            self.ccparser.parse("c"),
            ("c", "")
        )

    def test_fail(self):
        self.assertRaises(ParseError, self.ccparser.parse, "t")


class TestEndOfStringParser(TestCase):
    def setUp(self):
        a = CharacterParser("a")
        b = CharacterParser("b")
        c = CharacterParser("c")
        eos = EndOfStringParser()
        self.seq = SequenceParser(
            a,
            b,
            c,
            eos
        )

    def test_accept(self):
        self.assertEqual(
            self.seq.parse("abc"),
            (["a", "b", "c", ""], "")
        )

    def test_fail(self):
        self.assertRaises(ParseError, self.seq.parse, "abcd")
