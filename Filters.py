import re


class RegexFilter:
    
    def __init__(self, regex):
        self.regex = regex

    def match(self, text):
        return re.search(self.regex, text)