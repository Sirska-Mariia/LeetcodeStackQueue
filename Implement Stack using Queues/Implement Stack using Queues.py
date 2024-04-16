class Queue:
    def __init__(self):
        self.lt = []
        

    def push(self, x: int) -> None:
      self.lt.append(x)  

    def pop(self) -> int:
        if len(self.lt)>0:
            return self.lt.pop(0)
        return -1

    def top(self) -> int:
        if len(self.lt)>0:
            return self.lt[0]
        return -1
        
    def empty(self) -> bool:
        return len(self.lt)==0

class MyStack:

    def __init__(self):
        self.st = Queue()
        self.other = Queue()
        

    def push(self, x: int) -> None:
        self.st.push(x)

    def pop(self) -> int:
        while not self.st.empty():
                s = self.st.pop()
                self.other.push(s)
        while not self.other.empty():
                m = self.other.pop()
                if m != s:
                    self.st.push(m)
        return s
        

    def top(self) -> int:
        while not self.st.empty():
                self.other.push(self.st.pop())
        while not self.other.empty():
                m = self.other.pop()
                self.st.push(m)
        return m
        

    def empty(self) -> bool:
        return self.st.empty()
        
