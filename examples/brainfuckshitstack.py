#!/usr/bin/env python
from __future__ import print_function
import sys 
from braincore import Cell, Stack


def print_usage():
    print("usage: %s script.bfss")


if not len(sys.argv) > 1:
    print_usage()
    exit(1)


class CodeFeeder:

    def __init__(self, code=None):
        self.build_from(code)

    def get_ops(self):
        while self.loc_pointer < self.script_len:
            yield self.script[self.loc_pointer]
            self.loc_pointer += 1

    def __str__(self):
        return self.code

    def __repr__(self):
        return '<CodeFeeder of "%s">' % self

    def build_from(self, code=None):
        self.code = code or ""
        self.loc_pointer = 0
        self.script_len = len(script)


class ScriptExecutor:


    def __init__(self, script):
        self.script = script
        self.cell = Cell()
        self.stack = Stack()
        self.code = CodeFeeder(script)
        self.output = ''
        opcodes = {
            ">": self.cell.right,
            "<": self.cell.left,
            "+": self.cell.inc,
            "-": self.cell.dec,
            ".": self.print_char,
            ",": self.read_char,
            "[": self.jz,
            "]": self.jnz,
            "\\": self.push,
            "/": self.pop,
            "!": self.pvt
        }


    def run(self):
        for op in self.code.get_ops():
            self.opcodes.get(op, lambda: None)()
    
    def print_char(self):
        print(self.cell.read())

    def read_char(self):
        cell.write(ord(stdin.read(1)))

    def jz(self):
        if not self.cell:
            self.loc_pointer = self.script[self.loc_pointer:].index(']')

    def jnz(self):
        if self.cell:
            self.loc_pointer = self.script[:self.loc_pointer].rindex('[') - 1

    def push(self):
        self.stack.push(self.cell.read())

    def pop(self):
        self.cell.write(self.stack.pop())

    def pvt(self):
        old_stack = str(self.stack)
        old_code = str(self.code)
        self.stack = Stack(old_code)
        self.code.build_from(old_stack)


if __name__ == "__main__":
    script = open(sys.argv[1]).read()
    sexec = ScriptExecutor(script)
    sexec.run()

