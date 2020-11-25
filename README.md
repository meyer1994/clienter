# Clienter

[![Build Status](https://travis-ci.com/meyer1994/clienter.svg?branch=master)](https://travis-ci.com/meyer1994/clienter)
[![codecov](https://codecov.io/gh/meyer1994/clienter/branch/master/graph/badge.svg?token=GDPefbNqgR)](https://codecov.io/gh/meyer1994/clienter)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Build clients for REST APIs fast!

## Table of Contents

- [About](#about)
- [Install](#install)
- [Thanks](#thanks)


## About

I was tired of having to write boilerplate/custom clients for every REST endpoint available on the web. So, I decided to create something that do it for me. Here it is:

```py
import httpx
from clienter import Clienter


class GitHub(Clienter):
    def repos(self, owner, repo):
        """ GET /repos/{}/{} """


github = GitHub('https://api.github.com', httpx)
repo = github.repos('meyer1994', 'clienter').json()
print(repo)

# Output:
# {
#     'full_name': 'meyer1994/clienter',
#     'private': False,
#     ...
# }
```

Note that we pass the client we want to use to the object constructor. In this example, we are using [httpx][1]. It works with [requests][2] as well.

## Install

This project has no requirements :)

## Thanks

This project was inspired by the [OpenFeign][3] project.

[1]: https://www.python-httpx.org/
[2]: https://requests.readthedocs.io/en/master/
[3]: https://github.com/OpenFeign/feign
