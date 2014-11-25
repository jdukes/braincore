#/usr/bin/env python
from __future__ import print_function

try:
    from .brainfuck import BrainFuck
    from .brainfuckshitstack import BrainFuckShitStack
    from .brainloller import BrainLoller
except ImportError as e:
    print(e)
    del(e)
del(print_function)

__all__ = ["BrainFuck", "BrainFuckShitStack", "BrainLoller"]
