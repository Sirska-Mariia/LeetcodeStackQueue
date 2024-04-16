"""
freqstack
"""
from collections import deque
class FreqStack:

    def __init__(self):
        self.st = deque()
        self.dct = defaultdict(int)
        self.second = deque()

    def push(self, val: int) -> None:
        self.st.append(val)
        self.dct[val] += 1

    def pop(self) -> int:
        ind = 0
        for i in self.dct:
            if self.dct[i]>ind:
                ind = self.dct[i]
        while len(self.st)>0:
            m = self.st.pop()
            if self.dct[m] == ind:
                self.dct[m] -= 1
                break
            self.second.append(m)
        while len(self.second)!= 0:
            self.st.append(self.second.pop())
        return m
        
        #ind, lett, res, count = 0, 0, 0, 1
        #used = {}
        #d = self.st.copy()
        #while len(self.st) != 0:
        #    m = self.st.pop()
        #    if m not in used:
        #        k = d.count(m)
        #        if k > ind:
        #           ind, lett = k, m
        #           used[m] = ind
        #    self.second.append(m)
        #while len(self.second) != 0:
        #    m = self.second.pop()
        #    if m == lett and res == 0:
        #        if count == ind:
        #             res = 1
        #        else:
        #            self.st.append(m)
        #            count += 1
        #    else:
        #        self.st.append(m)
        #return lett
