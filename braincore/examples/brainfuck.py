#!/usr/bin/env python
from __future__ import print_function
from braincore import Cell
import sys

if sys.version_info.major == 3:
    _input = input
else:
    _input = raw_input

class BrainFuck:

    def __init__(self, script=None):
        self.setup(script)

    def setup(self, script=None):
        self.loc_pointer = 0
        self.cell = Cell()
        self.output = ''
        self.script = script or ''
        self.script_len = len(self.script)

    def run(self):
        for op in self.get_ops():
            if op == ">":
                self.cell.right()
            elif op == "<":
                self.cell.left()
            elif op == "+":
                self.cell.inc()
            elif op == "-":
                self.cell.dec()
            elif op == ".":
                self.print_char()
            elif op == ",":
                self.read_char()
            elif op == "[":
                self.jz()
            elif op == "]":
                self.jnz()

    def repl(self):
        while True:
            try:
                script = _input('fuck > ')
            except EOFError:
                break
            self.setup(script)
            self.run()
            print(repr(self.output))
            print('ord output:', [ ord(c) for c in self.output])
            print("current cell", ord(self.cell))
            print("current cell # ", ord(self.cell.pointer))

    def get_ops(self):
        while self.loc_pointer < self.script_len:
            yield self.script[self.loc_pointer]
            self.loc_pointer += 1
            
    def print_char(self):
        self.output += self.cell.read()

    def read_char(self):
        self.cell.write(ord(stdin.read(1)))

    def jz(self):
        if not self.cell:
            self.loc_pointer = self.script[self.loc_pointer:].index(']')

    def jnz(self):
        if self.cell:
            self.loc_pointer = self.script[:self.loc_pointer].rindex('[') - 1


def main():
    def print_usage():
        print("usage: %s script.bf")
    if not len(sys.argv) > 1:
        print_usage()
        exit(1)
    script = open(sys.argv[1]).read()
    sexec = BrainFuck(script)
    sexec.run()
    print(sexec.output)
            
if __name__ == "__main__":
    main()
