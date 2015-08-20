#!/usr/bin/env python

from toyparse.character import CharacterParser, NotCharacterParser
from toyparse.combinator import SequenceParser, OneOrMoreParser

string = \
"""------------------------
Author: Johannes
Date: 2015-08-20
------------------------
"""

seplineparser = SequenceParser(
    CharacterParser("-"),
    OneOrMoreParser(
        CharacterParser("-")
    ),
    CharacterParser("\n")
)

kvlineparser = SequenceParser(
    OneOrMoreParser(
        NotCharacterParser(":")
    ),
    CharacterParser(":"),
    OneOrMoreParser(
        CharacterParser(" ")
    ),
    OneOrMoreParser(
        NotCharacterParser("\n")
    ),
    CharacterParser("\n")
)

headerparser = SequenceParser(
    seplineparser,
    OneOrMoreParser(
        kvlineparser
    ),
    seplineparser
)

print(headerparser.parse(string))
