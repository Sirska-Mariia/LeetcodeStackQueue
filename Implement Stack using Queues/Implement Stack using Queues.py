"""
stack using queue
"""

class Queue:
    """
    queue
    """
    def __init__(self):
        self.lt = []

    def push(self, x: int) -> None:
        """
        adds new element
        """
        self.lt.append(x)

    def pop(self) -> int:
        """
        deletes first element
        """
        if len(self.lt)>0:
            return self.lt.pop(0)
        return -1

    def top(self) -> int:
        """
        returns first element
        """
        if len(self.lt)>0:
            return self.lt[0]
        return -1

    def empty(self) -> bool:
        """
        checks if empty
        """
        return len(self.lt)==0

class MyStack:
    """
    stack
    """
    def __init__(self):
        self.st = Queue()
        self.other = Queue()


    def push(self, x: int) -> None:
        """
        adds new element
        """
        self.st.push(x)

    def pop(self) -> int:
        """
        deletes new element
        """
        while not self.st.empty():
            s = self.st.pop()
            self.other.push(s)
        while not self.other.empty():
            m = self.other.pop()
            if m != s:
                self.st.push(m)
        return s

    def top(self) -> int:
        """
        returns last element
        """
        while not self.st.empty():
            self.other.push(self.st.pop())
        while not self.other.empty():
            m = self.other.pop()
            self.st.push(m)
        return m

    def empty(self) -> bool:
        """
        checks if stack is empty
        """
        return self.st.empty()
