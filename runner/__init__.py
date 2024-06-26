import json


class Item:
    def __init__(self, url, tries=0, info=None):
        self.url = url
        self.start = None
        self.tries = tries
        self.content = None
        self.info = info    # информация о потенциальном игроке, которая заполняется при парсинге сборных

    def __str__(self):
        return json.dumps({
            'url': self.url
        })
