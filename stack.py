# coding=utf-8

class Stack:
    """Implementation of Stack algorithm"""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)
        print("Items added:",self.items)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def remove(self):
        if self.is_empty():
            return None
        else:
            self.items.pop(0)
            print("Items left:",self.items)

    def size(self):
        print("Length:", len(self.items))

    def peek(self):
        if self.is_empty():
            return None
        else:
            print('Peek:', self.items[0])


if __name__ == '__main__':
  stack = Stack()
  stack.push(14)
  stack.push(5)
  stack.push(9)
  stack.peek()
  stack.size()
  stack.remove()
  stack.remove()
  stack.peek()
  stack.remove()
  stack.size()
  stack.peek()