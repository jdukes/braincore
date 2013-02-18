#!/usr/bin/env python

import sys
import Image
from braincore import Cell, IP

#(255,0,0) 	>
#(128,0,0) 	<
#(0,255,0) 	+
#(0,128,0) 	-
#(0,0,255) 	.
#(0,0,128) 	,
#(255,255,0) 	[
#(128,128,0) 	]
#(0,255,255) 	rotate IP to the right
#(0,128,128) 	rotate IP to the left 


def print_usage():
    print "usage: %s script.png" 


class ImageExecutor:

    def __init__(self, filename):
        self.im = Image.open(filename)
        if self.im.mode != "RGB":
            self.im = self.im.convert("RGB")
        self.ip = IP(self.im.size)
        self.cell = Cell()
        self.output = ''

    def run(self):
        for op in self.get_ops():
            if op == (255,0,0):
                self.cell.right()
            elif op == (128,0,0):
                self.cell.left()
            elif op == (0,255,0):
                self.cell.inc()
            elif op == (0,128,0):
                self.cell.dec()
            elif op == (0,0,255):
                self.print_char()
            elif op == (0,0,128):
                self.read_char()
            elif op == (255,255,0):
                self.jz()
            elif op == (128,128,0):
                self.jnz()
            elif op == (0,255,255):
                self.ip.right()
            elif op == (0,128,128):
                self.ip.left()

    def get_ops(self):
        for px in self.ip:
            yield self.im.getpixel(px)

    def print_char(self):
        self.output += self.cell.read()

    def read_char(self):
        cell.write(ord(stdin.read(1)))

    def jz(self):
        if not self.cell:
            for op in self.get_ops():
                if op == (128,128,0):
                    self.ip.next()
                    self.ip.reverse()
                    return
                elif op == (0,128,128):
                    self.ip.right()
                elif op == (0,255,255):
                    self.ip.left()

    def jnz(self):
        if self.cell:
            self.ip.reverse()
            for op in self.get_ops():
                if op == (255,255,0):
                    self.ip.reverse()
                    return
                elif op == (0,128,128):
                    self.ip.right()
                elif op == (0,255,255):
                    self.ip.left()
                

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print_usage()
        exit(1)
    filename = sys.argv[1]
    iexec = ImageExecutor(filename)
    iexec.run()
    print iexec.output
