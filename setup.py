
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'name': 'lightapp',
    'version': '0.1.0',
    'author': 'Raphi',
    'author_email': 'r.gaziano@gmail.com',
    'packages': ['lightapp', 'lightapp.tests'],
    'scripts': [], # any script in the bin directory
    'url': None,
    'download_url': None,
    'license': 'LICENSE.txt',
    'description': 'TODO',
    'long_description': open('README.txt').read(),
    'install_requires': [
    ]
}

setup(**config)
