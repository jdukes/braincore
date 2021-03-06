#!/usr/bin/env python
from setuptools import setup, find_packages
from datetime import datetime #for version string
import os
import sys
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'braincore'))
import braincore

now = datetime.now()


#fuck it, good enough edition
version="%s.%s.6" % (now.year, now.month) # PEP440 compliant

setup(name="braincore",
      version=version,
      description="Core objects needed for most brainfuck-like languages",
      url="https://github.com/jdukes/braincore",
      author="Josh Dukes",
      author_email="hex@neg9.org",
      license="MIT",
      entry_points = {
          'console_scripts': [
              'brainfuck=braincore.examples.brainfuck:main',
              'brainloller=braincore.examples.brainloller:main',
              'brainfuckshitstack=braincore.examples.brainfuckshitstack:main'],
      },
      keywords = "brainfuck, brainlol",
      long_description=braincore.__doc__,
      packages=find_packages())

