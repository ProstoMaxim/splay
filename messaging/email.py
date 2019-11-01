from filters import GmailComFilter, YandexRuFilter, MailRuFilter


EMAIL_FILTER_MAPPING = {
    'gmail.com': GmailComFilter,
    'yandex.ru': YandexRuFilter,
    'mail.ru': MailRuFilter,
}
DEFAULT_FILTER = GmailComFilter


class Email:
    def __init__(self, address, message):
        self.address = address
        self.message = message

    @property
    def _domain(self):
        return self.address.split('@')[-1].strip().lower()

    def prepare_message(self):
        EmailFilter = EMAIL_FILTER_MAPPING.get(self._domain) or DEFAULT_FILTER
        email_filter = EmailFilter()
        message = email_filter.process(self.message)

        return message

    def send(self):
        message = self.prepare_message()
        res = {
            "email": self.address,
            "content": message,
        }
        return res
