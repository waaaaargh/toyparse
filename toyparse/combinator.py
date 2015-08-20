from toyparse.parser import Parser, ParseError, EndOfString

class OneOrMoreParser(Parser):
    def __init__(self, parser):
        Parser.__init__(self)
        self._parser = parser

    def parse(self, text):
        results = []
        rest = text

        while True:
            try:
                result, rest = self._parser.parse(rest)
                results.append(result)
            except (ParseError, EndOfString):
                if len(results) == 0:
                    raise ParseError
                return results, rest


class AnyOfParser(Parser):
    def __init__(self, *args):
        Parser.__init__(self)
        self._parsers = args

    def parse(self, text):
        p_result, p_rest = "", ""
        valid_parser = False

        for parser in self._parsers:
            result, rest = "", ""
            try:
                result, rest = parser.parse(text)
                valid_parser = True
            except ParseError:
                pass

            if len(result) > len(p_result):
                p_result, p_rest = result, rest

        if not valid_parser:
            raise ParseError
        return p_result, p_rest


class SequenceParser(Parser):
    def __init__(self, *args):
        Parser.__init__(self)
        self._parsers = args

    def parse(self, text):
        results, rest = [], text
        for parser in self._parsers:
            tmp_result, rest = parser.parse(rest)
            results.append(tmp_result)

        return results, rest
