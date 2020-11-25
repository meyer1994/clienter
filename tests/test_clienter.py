from unittest import TestCase
from unittest.mock import MagicMock

from clienter import Clienter


class FakeClient(Clienter):
    def get(self, id):
        """ GET /test/{} """

    def put(self):
        """ PUT /test """

class TestClienter(TestCase):
    def test_get(self):
        """ Will perform a GET request """
        client = MagicMock()
        fake = FakeClient('base', client)
        fake.get(1)
        client.request.assert_called_once_with('GET', 'base/test/1')

    def test_put(self):
        """ Will perform a PUT request """
        client = MagicMock()
        fake = FakeClient('base', client)
        fake.put()
        client.request.assert_called_once_with('PUT', 'base/test')
