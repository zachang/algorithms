from collections import deque

class Queue:
    """Implementation of Queue algorithm using deque"""

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add items to list"""
        self.items.append(item)
        print("Items added:", list(self.items))

    def is_empty(self):
        """Checks if list is empty"""
        if len(self.items) == 0:
            return True
        else:
            return False

    def dequeue(self):
        """Removes item from list"""
        if self.is_empty():
            return None
        else:
            self.items.popleft()
            print("Items left:", list(self.items))

    def size(self):
        """Checks for the size of the list"""
        print("Length:", len(self.items))

    def peek(self):
        """Checks for single item in a list if not empty"""
        if self.is_empty():
            return None
        else:
            print('Peek:', self.items[0])


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(14)
    queue.enqueue(5)
    queue.enqueue(9)
    queue.peek()
    queue.size()
    queue.dequeue()
    queue.peek()
    queue.size()
    queue.dequeue()
    queue.peek()
    queue.size()
    queue.dequeue()
    queue.peek()
    queue.size()
