"""
queue using stacks
"""
class Stack():
    """
    stack
    """
    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        """
        adds new element
        """
        self.st.append(x)

    def pop(self) -> int:
        """
        deletes last element
        """
        if len(self.st)>0:
            return self.st.pop()
        return -1

    def peek(self) -> int:
        """
        returns last element
        """
        if len(self.st)>0:
            return self.st[-1]
        return -1

    def empty(self) -> bool:
        """
        checks if empty
        """
        return len(self.st) == 0


class MyQueue:
    """
    queue
    """
    def __init__(self):
        self.lt = Stack()
        self.other = Stack()

    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue.
        """
        self.lt.push(x)

    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns it
        """
        if not self.lt.empty():
            while not self.lt.empty():
                self.other.push(self.lt.pop())
            s = self.other.pop()
            while not self.other.empty():
                self.lt.push(self.other.pop())
            return s
        return -1

    def peek(self) -> int:
        """
        Returns the element at the front of the queue
        """
        if not self.lt.empty():
            while not self.lt.empty():
                self.other.push(self.lt.pop())
            s = self.other.pop()
            self.lt.push(s)
            while not self.other.empty():
                self.lt.push(self.other.pop())
            return s
        return -1

    def empty(self) -> bool:
        """
        Returns true if the queue is empty, false otherwise
        """
        return self.lt.empty()
