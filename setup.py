from setuptools import setup

import os
import sys
# sys.path.insert(0,os.path.join(os.path.dirname(__file__),'braincore'))
# import braincore

now = datetime.now()


def get_git_id():
    from subprocess import Popen, PIPE
    p = Popen(['git', 'show','-s','HEAD','--format=%h'],
              stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return out.strip(b'\n').decode('ascii')

version="%s%s.2a%s" % (now.year, now.month, get_git_id()) # PEP440 compliant

setup(name="braincore",
      version=version,
      description="Core objects needed for most brainfuck-like languages",
      url="https://github.com/jdukes/braincore",
      author="Josh Dukes",
      author_email="hex@neg9.org",
      license="MIT",
      keywords = "brainfuck, brainlol",
      long_description=hackercodecs.__doc__,
      packages=["braincore"])
