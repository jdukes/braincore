from setuptools import setup
from datetime import datetime #for version string
import os
import sys
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'braincore'))
import braincore

now = datetime.now()


# def get_git_id():
#     from subprocess import Popen, PIPE
#     p = Popen(['git', 'show','-s','HEAD','--format=%h'],
#               stdout=PIPE, stderr=PIPE)
#     out, err = p.communicate()
#     return out.strip(b'\n').decode('ascii')

#fuck it, good enough edition
version="%s.%s" % (now.year, now.month) # PEP440 compliant

setup(name="braincore",
      version=version,
      description="Core objects needed for most brainfuck-like languages",
      url="https://github.com/jdukes/braincore",
      author="Josh Dukes",
      author_email="hex@neg9.org",
      license="MIT",
      keywords = "brainfuck, brainlol",
      long_description=braincore.__doc__,
      packages=["braincore"])
