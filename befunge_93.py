from stack import Stack
import random


def math_op(a, b, current):
    operations = {
        '+': a + b,
        '-': b - a,
        '/': b // a if a != 0 else 0,
        '%': b % a if a != 0 else 0,
        '*': a * b
    }

    return operations[current]


def befunge(code):

    code = code.split('\n')
    output = []
    directions = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
    math = ['+', '-', '/', "*", "%"]
    logical = ["`", "!"]
    conditional = ["_", "|"]

    strmode = False

    length = len(code)
    width = len(code[0])

    current = code[0][0]
    coordinates = [0, 0]
    move = (0, 1)
    Stk = Stack()
    while current != '@':
        if strmode:
            if current == '"':
                strmode = False
            else:
                Stk.push(ord(current))
        else:
            print('coordinates', coordinates)
            print('pointer', current)
            print('output', output)
            print('Stack object', Stk.get_stack())

            if current.isdigit():
                Stk.push(int(current))

            elif current in math:
                Stk.push(math_op(Stk.pop(), Stk.pop(), current))

            elif current in logical:
                if current == '!':
                    Stk.push(int(Stk.pop == 0))
                elif current == '`':
                    num_0 = Stk.pop()
                    num_1 = Stk.pop()
                    Stk.push(int(num_1 > num_0))

            elif current in conditional:
                if current == '_':
                    val = Stk.pop()
                    if val == 0:
                        move = (0, 1)
                    else:
                        move = (0, -1)
                elif current == '|':
                    val = Stk.pop()
                    if val == 0:
                        move = (-1, 0)
                    else:
                        move = (1, 0)

            elif current in directions:
                move = directions.get(current)

            elif current == '?':
                move = random.choice((0, 1), (1, 0), (-1, 0), (0, -1))
            elif current == ':':
                Stk.duplicate()
            elif current == '$':
                Stk.pop()
            elif current == '.':
                num = Stk.pop()
                output.append(str(num))
            elif current == ',':
                letter = Stk.pop()
                output.append(str(chr(letter)))
            elif current == '#':
                move = (2 * move[0], 2 * move[1])
            elif current == '"':
                strmode = True
            elif current == "\\":
                Stk.swap()

            # elif current == 'p':

            # elif current == 'g':

        # move in a given direction
        coordinates[0] = coordinates[0] + move[0]
        coordinates[1] = coordinates[1] + move[1]

        # rationalize coordinates
        if coordinates[1] > width:
            coordinates[1] = coordinates[1] % width
            coordinates[0] = coordinates[0] + (coordinates[1] // width)
            if coordinates[0] > length:
                coordinates[0] = coordinates[0] % length
        if coordinates[0] > length:
            coordinates[0] = coordinates[0] % length
            coordinates[1] = coordinates[1] + (coordinates[0] // length)
            if coordinates[0] > width:
                coordinates[0] = coordinates[0] % width

        # set pointer
        current = code[coordinates[0]][coordinates[1]]
    return ''.join(output)




