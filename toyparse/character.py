from toyparse.parser import Parser, ParseError

class CharacterParser(Parser):
    def __init__(self, character):
        Parser.__init__(self)
        self._character = character

    def parse(self, text):
        # If text is empty, we are done.
        if len(text) == 0:
            raise ParseError

        # If the first character of `text` matches,
        # return the character as result and the rest
        # of the string as left.
        if text[0] == self._character:
            return self.transform(text[0]), text[1:]
        else:
            raise ParseError


class NotCharacterParser(Parser):
    def __init__(self, character):
        Parser.__init__(self)
        self._character = character

    def parse(self, text):
        # If text is empty, we are done.
        if len(text) == 0:
            raise ParseError

        # If the first character of `te-xt` doesn't match,
        # return the character as result and the rest
        # of the string as left.
        if text[0] != self._character:
            return self.transform(text[0]), text[1:]
        else:
            raise ParseError


class CharacterClassParser(Parser):
    def __init__(self, chars):
        Parser.__init__(self)
        self._chars = chars

    def parse(self, text):
        if len(text) == 0:
            raise ParseError(self, text)

        if text[0] in self._chars:
            return self.transform(text[0]), text[1:]
        else:
            raise ParseError


class EndOfStringParser(Parser):
    def parse(self, text):
        if len(text) > 0:
            raise ParseError

        return "", ""

