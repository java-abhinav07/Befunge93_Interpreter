class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

    def duplicate(self):
        if not self.is_empty():
            self.push(self.items[-1])
        self.push(0)

    def swap(self):
        if not self.is_empty():
            if len(self.items) > 1:
                num_0 = self.pop()
                num_1 = self.pop()
                self.push(num_0)
                self.push(num_1)
            elif len(self.items) == 1:
                num = self.pop()
                self.push(num)
                self.push(0)




