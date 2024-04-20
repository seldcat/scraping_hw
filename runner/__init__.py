import json


class Item:
    def __init__(self, url, tries=0, status=None):
        self.url = url
        self.start = None
        self.tries = tries
        self.content = None
        self.status = status  # championship/team/player

    def __str__(self):
        return json.dumps({
            'url': self.url,
            'status': self.status
        })

