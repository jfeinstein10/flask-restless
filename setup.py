# setup.py - packaging and distribution configuration for Flask-Restless
#
# Copyright 2011 Lincoln de Sousa <lincoln@comum.org>.
# Copyright 2012, 2013, 2014, 2015 Jeffrey Finkelstein
#           <jeffrey.finkelstein@gmail.com> and contributors.
#
# This file is part of Flask-Restless.
#
# Flask-Restless is distributed under both the GNU Affero General Public
# License version 3 and under the 3-clause BSD license. For more
# information, see LICENSE.AGPL and LICENSE.BSD.
"""
    Flask-Restless
    ~~~~~~~~~~~~~~

    Flask-Restless is a `Flask <http://flask.pocoo.org>`_ extension which
    facilitates the creation of ReSTful JSON APIs. It is compatible with models
    which have been defined using `SQLAlchemy <http://sqlalchemy.org>`_ or
    `Flask-SQLAlchemy <http://packages.python.org/Flask-SQLAlchemy>`_.

    For more information, check the World Wide Web!

      * `Documentation <https://flask-restless.readthedocs.org>`_
      * `PyPI listing <https://pypi.python.org/pypi/Flask-Restless>`_
      * `Source code repository <https://github.com/jfinkels/flask-restless>`_

"""
import codecs
import os.path
import re
from setuptools import setup

#: A regular expression capturing the version number from Python code.
VERSION_RE = r"^__version__ = ['\"]([^'\"]*)['\"]"

# TODO We require Flask version 1.0 or greater if we want Flask to recognize
# the JSON API mimetype as a form of JSON and therefore automatically be able
# to deserialize JSON to Python via the Request.get_json() method. On the other
# hand, we could keep the 0.10 requirement and simply rely on the ``force``
# keyword argument of that method, which also works around the limitations in
# MSIE8 and MSIE9...

#: The installation requirements for Flask-Restless. Flask-SQLAlchemy is not
#: required, so the user must install it explicitly.
REQUIREMENTS = ['flask>=0.10', 'sqlalchemy>=0.8', 'python-dateutil>2.2',
                'mimerender>=0.5.2']

#: The absolute path to this file.
HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """Reads the entire contents of the file whose path is given as `parts`."""
    with codecs.open(os.path.join(HERE, *parts), 'r') as f:
        return f.read()


def find_version(*file_path):
    """Returns the version number appearing in the file in the given file
    path.

    Each positional argument indicates a member of the path.

    """
    version_file = read(*file_path)
    version_match = re.search(VERSION_RE, version_file, re.MULTILINE)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    author='Jeffrey Finkelstein',
    author_email='jeffrey.finkelstein@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Database :: Front-Ends',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    description='A Flask extension for easy ReSTful API generation',
    download_url='http://pypi.python.org/pypi/Flask-Restless',
    install_requires=REQUIREMENTS,
    include_package_data=True,
    keywords=['ReST', 'API', 'Flask'],
    license='GNU AGPLv3+ or BSD',
    long_description=__doc__,
    name='Flask-Restless',
    platforms='any',
    packages=['flask_restless'],
    test_suite='nose.collector',
    tests_require=['nose'],
    url='http://github.com/jfinkels/flask-restless',
    version=find_version('flask_restless', '__init__.py'),
    zip_safe=False
)
