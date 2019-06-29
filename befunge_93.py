from stack import Stack
import random


def math_op(a, b, current):
    if current == '+':
        return a + b
    elif current == '-':
        return a - b
    elif current == '/':
        if a == 0: return 0
        return b // a
    elif current == '%':
        if a == 0: return 0
        return b % a
    elif current == '*':
        return a * b


def befunge(code):
    code = code.split('\n')
    output = []
    directions = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
    math = ['+', '-', '/', "*", "%",]
    logical = ["`", "!"]
    conditional = ["_", "|"]

    length = len(code)
    x_len = []
    for i in range(length):
        x_len.append(len(code[i]))
    width = max(x_len)

    current = code[0][0]
    coordinates = [0, 0]
    Stk = Stack()
    while current != '@':

        if current in range(10):
            Stk.push(current)
            print(Stk.get_stack())

        elif current in math:
            math_op(Stk.pop(), Stk.pop(), current)

        elif current in logical:
            if current == '!':
                val = Stk.pop()
                if val == 0:
                    Stk.push(1)
                else:
                    Stk.push(0)
            elif current == '`':
                num_0 = Stk.pop()
                num_1 = Stk.pop()
                Stk.push(int(num_1>num_0))

        elif current in conditional:
            if current == '_':
                val = Stk.pop()
                if val == 0:
                    move = (0, 1)
                else:
                    move = (0, -1)
            elif current == '|':
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
            num = ord(Stk.pop())
            output.append(num)

        elif current == ',':
            letter = chr(Stk.pop())
            output.append(letter)

        elif current == '#':
            move = (0, 2)

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


print(befunge('>987v>.v\nv456<  :\n>321 ^ _@'))












