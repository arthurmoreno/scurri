import sys
import setuptools
from distutils.core import setup


setup(
    name='uk-postcodes',
    version='0.0.1',
    author='Arthur Moreno',
    author_email='morenoarthur@gmail.com',
    url='https://github.com/arthurmoreno/scurri/',
    description=(
        'Python library for formatting and validating'
        'uk post codes.'
    ),
    py_modules=['ukpostcodes'],
    license='GPL3',
    keywords=['uk', 'postcode', 'validation', 'formatting'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
