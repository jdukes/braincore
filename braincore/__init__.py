#!/usr/bin/env python
"""This code implements the core objects needed for most brainfuck-like languages.

The number of cells for this implementation is infinite, the max value
of cells defaults to 255.
"""


class IP:

    def __init__(self, max_xy):
        self.direction = "east"
        self.directions = ["east", "south", "west", "north"]
        self.vectors = [(1, 0), (0, +1), (-1, 0), (0, -1)]
        self.vector_map = dict(zip(self.directions, self.vectors))
        self.x = -1 # incriments first
        self.y = 0
        self.max_x, self.max_y = max_xy #1 indexed, remove one later
        self.max_x -= 1 
        self.max_y -= 1

    def __iter__(self):
        return self

    def turn(self, direction):
        if direction == "left":
            idx = (self.directions.index(self.direction) - 1) % 4
        elif direction == "right":
            idx = (self.directions.index(self.direction) + 1) % 4
        elif direction == "reverse":
            idx = (self.directions.index(self.direction) + 2) % 4
        self.direction = self.directions[idx]

    def left(self):
        self.turn("left")

    def right(self):
        self.turn("right")
        
    def reverse(self):
        self.turn("reverse")

    def get_vector(self):
        return self.vector_map[self.direction]

    def next(self):
        vx, vy = self.get_vector()
        self.x += vx
        self.y += vy
        if self.x > self.max_x \
           or self.y > self.max_y \
           or self.y < 0 \
           or self.x < 0:
            raise StopIteration
        return (self.x, self.y)


class Stack:

    def __init__(self, contents=None):
        self.contents = contents or []

    def __str__(self):
        return ''.join(self.contents)

    def __repr__(self):
        return '<Stack of "%s">' % self

    def push(self, val):
        self.contents.push(val)

    def pop(self):
        return self.contents.pop()


class Cell:

    def __init__(self, max_val=255):
        self.pointer = 0
        self.max_val = max_val
        self.vals = {}

    def __getitem__(self, idx):
        return self.vals.get(idx, 0)

    def __setitem__(self, idx, val):
        self.vals[idx] = val

    def __add__(self, val):
        return self.vals.get(self.pointer, 0) +  val

    def __sub__(self, val):
        return self.vals.get(self.pointer, 0) - val

    def __bool__(self):
        return self[self.pointer] > 0

    def __nonzero__(self):
        return self.__bool__()

    def __repr__(self):
        return self.read()

    def right(self):
        self.shift(+1)

    def left(self):
        self.shift(-1)

    def shift(self, direction):
        self.pointer = self.pointer + direction

    def inc(self):
        self.inc_or_dec(1)

    def dec(self):
        self.inc_or_dec(-1)

    def inc_or_dec(self, val):
        self.vals[self.pointer] = (self.vals.get(self.pointer, 0) + val) \
                                  % self.max_val

    def read(self):
        return chr(self[self.pointer])

    def write(self, val):
        self[self.pointer] = val

        
