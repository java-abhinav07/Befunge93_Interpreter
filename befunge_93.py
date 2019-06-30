from stack import Stack
import random


def math_op(a, b, current):
    operations = {
        '+': a+ b,
        '-': a - b,
        '/': b // a if a != 0 else 0,
        '%': b % a if a != 0 else 0,
        '*': a * b
    }

    return operations[current]


def befunge(code):

    code = code.split('\n')
    output = []
    directions = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
    math = ['+', '-', '/', "*", "%",]
    logical = ["`", "!"]
    conditional = ["_", "|"]
    move = (0, 1)
    strmode = False

    length = len(code)
    x_len = []
    for i in range(length):
        x_len.append(len(code[i]))
    width = max(x_len)

    current = code[0][0]
    coordinates = [0, 0]
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
                        move(-1, 0)
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
                while not Stk.is_empty():
                    num = Stk.pop()
                    print('popped', num)
                    output.append(num)
            elif current == ',':
                while not Stk.is_empty():
                    letter = Stk.pop()
                    output.append(chr(letter))
            elif current == '#':
                move = (2 * move[0], 2 * move[1])
            elif current == '"':
                strmode = True

            # elif current == 'p':

            # elif current == 'g':

        # move in a given direction
        coordinates[0] = coordinates[0] + move[0]
        coordinates[1] = coordinates[1] + move[1]

        # rationalize coordinates
        coordinates = [(length+coordinates[0])%length, (width + coordinates[1])%width]

        # set pointer
        current = code[coordinates[0]][coordinates[1]]

    return ''.join(output)


print(befunge('64+"!dlroW ,olleH">:#,_@'))











