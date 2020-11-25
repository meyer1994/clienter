import inspect
import logging
import functools
from typing import Tuple, List

logger = logging.getLogger('Clienter')
logger.setLevel(logging.INFO)


def docparse(doc: str) -> Tuple[str, str]:
    doc = doc.split('\n')[0].strip()
    return doc.split(' ')


def methods(cls: object) -> List[callable]:
    methods = inspect.getmembers(cls, predicate=inspect.ismethod)
    return [meth for name, meth in methods if not name.startswith('_')]


def request(cls: object, method: callable) -> callable:
    verb, path = docparse(method.__doc__)

    @functools.wraps(method)
    def wrapper(*args: tuple, **kwargs: dict) -> object:
        logger.info('Request: %s %s', verb, path)
        endpoint = cls._base + path.format(*args)
        return cls._client.request(verb, endpoint, **kwargs)

    return wrapper


class Clienter(object):
    def __init__(self, base: str, client: object):
        super(Clienter, self).__init__()
        self._base = base
        self._client = client

        for method in methods(self):
            requester = request(self, method)
            setattr(self, method.__name__, requester)
