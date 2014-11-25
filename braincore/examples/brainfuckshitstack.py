#!/usr/bin/env python
from __future__ import print_function
import sys 
from braincore import Cell, Stack


class CodeFeeder:

    def __init__(self, script=None):
        self.build_from(script)

    def get_ops(self):
        while self.loc_pointer < self.script_len:
            yield self.script[self.loc_pointer]
            self.loc_pointer += 1

    def __str__(self):
        return self.script

    def __repr__(self):
        return '<ScriptFeeder of "%s">' % self

    def build_from(self, script=None):
        self.script = script or ""
        self.loc_pointer = 0
        self.script_len = len(script)

    def jump_ahead(self):
        self.loc_pointer = self.script[self.loc_pointer:].index(']')

    def jump_back(self):
        self.loc_pointer = self.script[:self.loc_pointer].rindex('[') - 1


class BrainFuckShitStack:


    def __init__(self, script, out_fd=sys.stdout):
        self.out = out_fd
        self.script = script
        self.cell = Cell()
        self.stack = Stack()
        self.code = CodeFeeder(script)
        self.output = ''
        self.opcodes = {
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
        out.write(self.cell.read())
        out.flush()

    def read_char(self):
        cell.write(ord(stdin.read(1)))

    def jz(self):
        if not self.cell:
            self.code.jump_ahead()
            
    def jnz(self):
        if self.cell:
            self.code.jump_back()

    def push(self):
        self.stack.push(self.cell.read())

    def pop(self):
        self.cell.write(self.stack.pop())

    def pvt(self):
        old_stack = str(self.stack)
        old_code = str(self.code)
        self.stack = Stack(old_code)
        self.code.build_from(old_stack)


def main():
    if not len(sys.argv) > 1:
        print_usage()
        exit(1)
    script = open(sys.argv[1]).read()
    sexec = BrainFuckShitStack(script)
    sexec.run()
    print()
    
        
if __name__ == "__main__":
    main()
