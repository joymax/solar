import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "solar",
    version = "0.0.3",
    author = "Alexander Koval",
    author_email = "kovalidis@gmail.com",
    description = ("A library to use solr in python projects."),
    license = "BSD",
    keywords = "solr solar pysolr",
    url = "https://github.com/anti-social/solar",
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Libraries",
        "License :: OSI Approved :: BSD License",
    ],
)
