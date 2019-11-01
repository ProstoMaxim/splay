import re


class RegexFilter:
    PATTERN = r''
    REPL = r''

    def process(self, message):
        result = re.sub(self.PATTERN, self.REPL, message, flags=re.IGNORECASE)
        return result


class GmailComFilter(RegexFilter):
    PATTERN = r'[^.?!]*(?<=[.?\s!])offer(?=[\s.?!])[^.?!]*[.?!]'


class YandexRuFilter(RegexFilter):
    PATTERN = r'<img src="(\S+)"\s*/>'
    REPL = r'\1'


class MailRuFilter(RegexFilter):
    PATTERN = r'(<img src="\S+)\.gif("\s*/>)'
    REPL = r'\1.png\2'
