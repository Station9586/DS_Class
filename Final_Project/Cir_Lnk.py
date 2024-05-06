class Node: 
    def __init__ (self, a) -> None: 
        self.val = a;
        self.nxt = None;



class CircularLinkedList: 
    def __init__ (self) -> None: 
        self.head = None;
        self.tail = None;

    def __len__ (self) -> int: 
        if (not self.head): return 0;
        cur = self.head;
        ret = 1;
        while (cur.next != self.head): 
            cur = cur.next;
            ret += 1;
        return ret;

    def Print (self) -> None: 
        cur = self.head;
        while (True): 
            print(cur.val, end = " \n"[cur == self.tail]);
            if (cur == self.tail): break;
            cur = cur.next;

    def insert (self, a) -> None: 
        nw = Node(a);
        if (not self.head): 
            self.head = nw;
            self.tail = nw;
            return;

        self.tail.next = nw;
        self.tail = self.tail.next;
        self.tail.next = self.head;

    def delete (self, a) -> None: 
        cur = self.head;
        prev = None;
        while (cur.val != a): 
            prev = cur;
            cur = cur.next;
            if (cur == self.head): 
                print(f"Val {a} not found.");
                return;
        if (cur == self.head): 
            self.head = self.head.next;
            self.tail.next = self.head;
        elif (cur == self.tail): 
            prev.next = self.head;
            self.tail = prev;
        else: prev.next = cur.next;

if __name__ == "__main__": 
    c = CircularLinkedList();
    num = [4, 8, 7, 6, 3, 3, 1, 4, 1, 5, 9];

    for i in num: c.insert(i);
    c.Print();
    print();

    c.delete(7);
    c.Print();
    print();
    
    c.delete(20);
    c.Print();