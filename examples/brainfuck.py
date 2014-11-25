#!/usr/bin/env python
from __future__ import print_function
import sys 
from braincore import Cell


def print_usage():
    print("usage: %s script.bf")


if not len(sys.argv) > 1:
    print_usage()
    exit(1)


class ScriptExecutor:

    def __init__(self, script):
        self.loc_pointer = 0
        self.script = script
        self.script_len = len(script)
        self.cell = Cell()
        self.output = ''

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
            elif op =="]":
                self.jnz()

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


if __name__ == "__main__":
    script = open(sys.argv[1]).read()
    sexec = ScriptExecutor(script)
    sexec.run()
    print(sexec.output)
