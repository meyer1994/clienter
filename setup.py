from setuptools import find_packages, setup

setup(
    name='clienter',
    version='0.0.1',
    description='Build ',
    url='https://github.com/meyer1994/clienter',
    download_url='https://github.com/meyer1994/clienter/archive/0.0.1.tar.gz',
    author='João Vicente Meyer',
    license='Unlicense',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    keywords='requests httpx rest api http',
    packages=find_packages(
        exclude=['tests']
    ),
    install_requires=[],
    python_requires='>=3.6',
)
