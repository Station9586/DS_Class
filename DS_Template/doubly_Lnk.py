class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.lhs = None
        self.rhs = None

class DoublyLinkedList: 
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __len__ (self) -> int: 
        ret = 0
        cur = self.head
        while (True): 
            ret += 1
            if (cur == self.tail): break
            cur = cur.rhs
        return ret
    
    def push_front (self, data) -> None: 
        nw = Node(data)
        if (self.head == None): 
            self.head = nw
            self.tail = nw
        else: 
            cur = self.head
            self.head.lhs = nw
            self.head = nw
            self.head.rhs = cur
            self.head.lhs = self.tail
            self.tail.rhs = self.head
    
    def push_back (self, data) -> None: 
        nw = Node(data)
        if (self.head == None): 
            self.head = nw
            self.tail = nw
        else: 
            cur = self.tail
            self.tail.rhs = nw
            self.tail = self.tail.rhs
            self.tail.lhs = cur
            self.tail.rhs = self.head
            self.head.lhs = self.tail
    
    def delete (self, a) -> None: 
        cur = self.head
        prev = None
        while (cur.data != a): 
            prev = cur
            cur = cur.rhs
            if (cur == self.head): 
                print(f"data {a} not found.")
                return
        if (cur == self.head): 
            self.head = self.head.rhs
            self.head.lhs = self.tail
            self.tail.rhs = self.head
        elif (cur == self.tail): 
            self.tail = prev
            self.tail.rhs = self.head
            self.head.lhs = self.tail
        else: 
            prev.rhs = cur.rhs
            cur.rhs.lhs = prev

    def Print (self) -> None: 
        cur = self.head
        if (cur is None): return
        while (True): 
            print(cur.data, end = ",\n"[cur == self.tail])
            if (cur == self.tail): break
            cur = cur.rhs

    def Print2(self) -> None: 
        cur = self.tail
        if (cur is None): return
        while (True): 
            print(cur.data, end = ",\n"[cur == self.tail])
            if (cur == self.head): break
            cur = cur.lhs

    def Search (self, a) -> bool: 
        cur = self.head
        if (cur == None): return False
        while (True): 
            if (cur.data == a): return True
            if (cur == self.tail): break
            cur = cur.rhs
        return False