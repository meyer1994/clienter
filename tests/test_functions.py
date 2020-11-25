from unittest import TestCase
from unittest.mock import MagicMock

import clienter


class TestFunctions(TestCase):
    def test_docparse(self):
        """ Correctly parses docstring """
        docstring = 'GET /nice'
        verb, path = clienter.docparse(docstring)
        self.assertEqual(verb, 'GET')
        self.assertEqual(path, '/nice')

    def test_methods(self):
        """ Returns a list of public methods """
        class Fake(object):
            def public(self):
                pass

            def _private(self):
                pass

        fake = Fake()
        methods = clienter.methods(fake)
        self.assertListEqual(methods, [fake.public])

    def test_requests(self):
        """ Returns a new callable that calls a client """
        class Fake(object):
            _client = MagicMock()
            _base = 'base'

            def method(self, id):
                """ GET /nice/{} """

        fake = Fake()
        request = clienter.request(fake, fake.method)
        request('1', json={})
        Fake._client.request\
            .assert_called_once_with('GET', 'base/nice/1', json={})
