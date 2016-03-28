import requests


class Client(object):

    def _get(self, url, *args, **kwargs):
        return requests.get(url, *args, **kwargs)

    def get_issue(self, issue):
        pass
