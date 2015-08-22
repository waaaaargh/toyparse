import pprint

class ParseError(Exception):
    def __init__(self, parser, got):
        Exception.__init__(self)
        self.parser = parser
        self.got = got

class EndOfString(Exception):
    pass

class Parser:
    def parse(text):
        raise NotImplemented

    def transform(self, result):
        return result

    def describe(self):
        return {"name": self.__class__.__name__}

    def pprint(self):
        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(self.describe())
