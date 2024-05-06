class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.nxt = None

class Queue: 
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __len__ (self) -> int: 
        ret = 0
        cur = self.head
        while (cur != None): 
            ret += 1
            cur = cur.nxt
        return ret
    
    def push (self, data) -> None: 
        nw = Node(data)
        if (self.head == None): 
            self.head = nw
            self.tail = nw
        else: 
            self.tail.nxt = nw
            self.tail = self.tail.nxt
    
    def pop (self) -> None: 
        if (len(self) == 1): 
            self.head = None
            self.tail = None
        else: self.head = self.head.nxt
    
    def front (self):  return self.head.data 

    def empty (self) -> bool: return self.head == None

    def Print (self): 
        cur = self.head
        if (cur is None): 
            print("None")
            return
        while (cur != None): 
            print(cur.data, end = ",\n"[cur.nxt == None])
            cur = cur.nxt

class Stack: 
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __len__ (self) -> int: 
        ret = 0
        cur = self.head
        while (cur != None): 
            ret += 1
            cur = cur.nxt
        return ret

    def push (self, data) -> None: 
        nw = Node(data)
        if (self.head == None): 
            self.head = nw
            self.tail = nw
        else: 
            prev = self.head
            self.head = nw
            self.head.nxt = prev
    
    def pop (self) -> None: 
        if (len(self) == 1): 
            self.head = None
            self.tail = None
        else: self.head = self.head.nxt
    
    def top (self): return self.head.data
    
    def empty (self) -> bool: return self.head == None