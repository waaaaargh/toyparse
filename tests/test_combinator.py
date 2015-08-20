from unittest import TestCase
from toyparse.combinator import OneOrMoreParser, AnyOfParser, SequenceParser
from toyparse.character import CharacterParser
from toyparse.parser import ParseError

class TestOneOrMoreParser(TestCase):
    def setUp(self):
        cparse = CharacterParser("c")
        self.oomparser = OneOrMoreParser(cparse)

    def test_accept(self):
        self.assertEqual(
            self.oomparser.parse("cccb"),
            (["c", "c", "c"], "b")
        )
        self.assertEqual(
            self.oomparser.parse("ccc"),
            (["c", "c", "c"], "")
        )

    def test_fail(self):
        self.assertRaises(ParseError, self.oomparser.parse, "b")
        self.assertRaises(ParseError, self.oomparser.parse, "")


class TestAnyOfParser(TestCase):
    def setUp(self):
        a = CharacterParser("a")
        b = CharacterParser("b")
        c = CharacterParser("c")
        self.aoparser = AnyOfParser(a,b,c)

    def test_accept(self):
        self.assertEqual(
            self.aoparser.parse("a"),
            ("a", "")
        )
        self.assertEqual(
            self.aoparser.parse("b"),
            ("b", "")
        )
        self.assertEqual(
            self.aoparser.parse("c"),
            ("c", "")
        )

    def test_fail(self):
        self.assertRaises(ParseError, self.aoparser.parse, "d")


class TestSequenceParser(TestCase):
    def setUp(self):
        a = CharacterParser("a")
        b = CharacterParser("b")
        c = CharacterParser("c")
        self.seqparser = SequenceParser(a, b, c)

    def test_accept(self):
        self.assertEqual(
            self.seqparser.parse("abc"),
            (["a", "b", "c"], "")
        )

    def test_fail(self):
        self.assertRaises(ParseError, self.seqparser.parse, "add")
        self.assertRaises(ParseError, self.seqparser.parse, "ddd")
