#!/usr/bin/env python

from toyparse.parser import Parser
from toyparse.character import CharacterParser, NotCharacterParser, CharacterClassParser
from toyparse.combinator import SequenceParser, OneOrMoreParser, AnyOfParser

from string import ascii_letters, digits, punctuation

string = \
"""------------------------
Author: Johannes
Date: 2015-08-20
------------------------
"""

class WordParser(OneOrMoreParser):
    def __init__(self):
        OneOrMoreParser.__init__(self,
            CharacterClassParser(
                ascii_letters+digits+"-"
            )
        )

    def transform(self, result):
        return "".join(result)

seplineparser = SequenceParser(
    CharacterParser("-"),
    OneOrMoreParser(
        CharacterParser("-")
    ),
    CharacterParser("\n")
)

class KVLineParser(SequenceParser):
    def __init__(self):
        SequenceParser.__init__(self,
            WordParser(),
            CharacterParser(":"),
            OneOrMoreParser(
                CharacterParser(" ")
            ),
            WordParser(),
            CharacterParser("\n")
        )

    def transform(self, result):
        return (result[0], result[3])


headerparser = SequenceParser(
    seplineparser,
    OneOrMoreParser(
        KVLineParser()
    ),
    seplineparser
)

print(headerparser.parse(string))
