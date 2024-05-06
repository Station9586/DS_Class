class Node: 
    def __init__(self, data) -> None:
        self.data = data;
        self.lhs = None;
        self.rhs = None;

class DoublyLinkedList: 
    def __init__(self) -> None:
        self.head = None;
        self.tail = None;

    def __len__ (self) -> int: 
        ret = 0;
        cur = self.head;
        while (True): 
            ret += 1;
            if (cur == self.tail): break;
            cur = cur.rhs;
        return ret;
    
    def push_front (self, data) -> None: 
        nw = Node(data);
        if (self.head == None): 
            self.head = nw;
            self.tail = nw;
        else: 
            cur = self.head;
            self.head.lhs = nw;
            self.head = nw;
            self.head.rhs = cur;
            self.head.lhs = self.tail;
            self.tail.rhs = self.head;
    
    def push_back (self, data) -> None: 
        nw = Node(data);
        if (self.head == None): 
            self.head = nw;
            self.tail = nw;
        else: 
            cur = self.tail;
            self.tail.rhs = nw;
            self.tail = self.tail.rhs;
            self.tail.lhs = cur;
            self.tail.rhs = self.head;
            self.head.lhs = self.tail;
    
    def delete (self, a) -> None: 
        cur = self.head;
        prev = None;
        while (cur.data != a): 
            prev = cur;
            cur = cur.rhs;
            if (cur == self.head): 
                print(f"class {a} not found.");
                return;
        if (cur == self.head): 
            self.head = self.head.rhs;
            self.head.lhs = self.tail;
            self.tail.rhs = self.head;
        elif (cur == self.tail): 
            self.tail = prev;
            self.tail.rhs = self.head;
            self.head.lhs = self.tail;
        else: 
            prev.rhs = cur.rhs;
            cur.rhs.lhs = prev;

    def Print (self) -> None: 
        cur = self.head;
        if (cur is None): 
            print("Empty course.")
            return;
        while (True): 
            print(cur.data, end = ",\n"[cur == self.tail]);
            if (cur == self.tail): break;
            cur = cur.rhs;

    def Print2(self) -> None: 
        cur = self.tail;
        while (True): 
            print(cur.data);
            if (cur == self.head): break;
            cur = cur.lhs;

    def Search (self, a) -> bool: 
        cur = self.head;
        if (cur == None): return False;
        while (True): 
            if (cur.data == a): return True;
            if (cur == self.tail): break;
            cur = cur.rhs;
        return False;

    # def swap (self, a, b) -> None: 
    #     if (a == b): return;
    #     if (a.lhs == self.tail): self.head = b;
    #     a.lhs.rhs = b;
    #     if (b.rhs == self.head): self.tail = a;
    #     b.rhs.lhs = a;
    #     a.rhs, b.rhs = b.rhs, a;
    #     a.lhs, b.lhs = b, a.lhs;

    # def sort (self) -> None: 
    #     if (self.head == None): return;
    #     for i in range(len(self) + 1): 
    #         cur = self.head;
    #         while (cur != self.tail):
    #             if (cur.data < cur.rhs.data): self.swap(cur, cur.rhs);
    #             else: cur = cur.rhs;
 
# a = DoublyLinkedList();

# for i in range(5): a.push_back(i);

# for i in range(60, -60, -10): a.push_front(i);
# a.Print()
# print()
# # a.Print2();

# a.sort();
# a.Print();
# print();

# print(f"len: {len(a)}");

# a.delete(60);
# a.Print();
# print();

# a.delete(30);
# a.Print();
# print();

# a.delete(100);
# a.Print();
# print();