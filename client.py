import ssl
import requests
from requests.auth import HTTPBasicAuth


class Client(object):

    # TODO: make it configurable
    base_url = 'https://jira.atlassian.com/rest/api/2'

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password
    def __init__(self):
        pass

    # def _get(self, url, *args, **kwargs):
    #     if not all([self.username, self.password]):
    #         raise ValueError("Login credentials not provided")
    #     kwargs['auth'] = HTTPBasicAuth(self.username, self.password)
    #     kwargs['params'] = kwargs.get('params', {})
    #     return requests.get(url, *args, **kwargs)
    #
    # def get_issue(self, issue):
    #     url = self.base_url + '/issue/{}'.format(issue)
    #     return self._get(url)
