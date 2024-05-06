class MinHeap: 
    def __init__ (self) -> None: 
        self.heap = [-1];
        self.size = 0;
        
    def swap (self, i, j) -> None: self.heap[i], self.heap[j] = self.heap[j], self.heap[i];

    def swim (self, n) -> None: 
        while (n): 
            if (self.heap[n] >= self.heap[n >> 1]): break;
            self.swap(n, n >> 1);
            n >>= 1;

    def insert (self, a) -> None: 
        self.heap.append(a);
        self.size += 1;
        self.swim(self.size);

    def push (self, i, n) -> None: 
        while (i << 1 <= n): 
            j = i << 1;
            if (j < n and self.heap[j + 1] < self.heap[j]): j += 1;
            if (self.heap[j] < self.heap[i]): self.swap(j, i);
            i = j;

    def pop (self) -> int: 
        ret = self.heap[1];
        self.heap[1] = self.heap[self.size];
        self.heap.pop();
        self.size -= 1;
        self.push(1, self.size);
        return ret;

    def delete (self, a, last) -> None: 
        for i in range(len(self.heap)): 
            if (self.heap[i] == a): 
                idx = i;
                break;

        self.heap[idx] = last;
        if (idx > 1 and self.heap[idx] < self.heap[idx >> 1]): self.swim(idx);
        else: self.push(idx, self.size);

class Node: 
    def __init__(self, val, name) -> None:
        self.val = val;
        self.name = name;

class MaxHeap: 
    def __init__ (self) -> None: 
        self.heap = [Node(-1, "None")];
        self.size = 0;
    def swap (self, i, j) -> None: self.heap[i], self.heap[j] = self.heap[j], self.heap[i];

    def swim (self, n) -> None: 
        while (n > 1): 
            if (self.heap[n].val <= self.heap[n >> 1].val): break;
            self.swap(n, n >> 1);
            n >>= 1;

    def insert (self, a, name) -> None: 
        self.heap.append(Node(a, name));
        self.size += 1;
        self.swim(self.size);

    def push (self, i, n) -> None: 
        while (i << 1 <= n): 
            j = i << 1;
            if (j < n and self.heap[j + 1].val > self.heap[j].val): j += 1;
            if (self.heap[j].val > self.heap[i].val): self.swap(j, i);
            i = j;

    def pop (self) -> Node: 
        ret = self.heap[1];
        self.heap[1] = self.heap[self.size];
        self.heap.pop();
        self.size -= 1;
        self.push(1, self.size);
        return ret; 

    def delete (self, name, val, last) -> None: 
        for i in range(len(self.heap) + 1): 
            if (self.heap[i].name == name and self.heap[i].val + 1 == val): 
                idx = i;
                break;
        self.heap[idx] = last;
        self.heap.pop();
        self.size -= 1;
        if (idx > self.size): return;
        if (idx > 1 and self.heap[idx].val > self.heap[idx >> 1].val): self.swim(idx);
        else: self.push(idx, self.size);

    def modify (self, name, val): 
        self.delete(name, val, self.heap[-1]);
        self.insert(val, name);

    def search (self, name): 
        for i in range(len(self.heap)): 
            if (self.heap[i].name == name): return 1;
        return 0;

    def get_first_k_value (self, k): 
        if (k > self.size): 
            print("k cannot be larger than number of courses been chosen.");
            return;
        tmp = [];
        for i in range(k): tmp.append(self.pop());
        ret = tmp[0::];
        for i in range(k): self.insert(tmp[i].val, tmp[i].name);
        return ret;


# class Deap: 
#     def __init__ (self) -> None: 
#         self.min_heap = MinHeap();
#         self.max_heap = MaxHeap();
#         self.mp = dict();
#         self.nw = 1;

#     def isLeft (self, n) -> bool: 
#         if (n == 0): return 1;
#         while (n): 
#             if (not n & 1): return 1;
#             n >>= 1;
#         return 0;

#     def insert (self, a) -> None: 
#         n = self.min_heap.size;
#         m = self.max_heap.size;
#         if (self.isLeft(n) or n == m): 
#             self.min_heap.insert(a);
#             self.mp[a] = 1;
#             self.nw = 1;
#         else: 
#             self.max_heap.insert(a);
#             self.mp[a] = 2;
#             self.nw = 2;

#     def delete (self, a) -> None: 
#         if (a not in self.mp): 
#             print(f"val {a} not found");
#             return;
#         if (self.mp[a] == 1): 
#             if (self.nw == 1): 
#                 self.min_heap.delete(a, self.min_heap.heap[-1]);
#                 self.min_heap.heap.pop();
#                 self.min_heap.size -= 1;
#                 if (self.min_heap.size == self.max_heap.size): self.nw = 2;
#                 else: self.nw = 1;
#             else: 
#                 self.min_heap.delete(a, self.max_heap.heap[-1]);
#                 self.max_heap.heap.pop();
#                 self.max_heap.size -= 1;
#                 if (not self.isLeft(self.max_heap.size)): self.nw = 1;
#                 else: self.nw = 2;
#         else: 
#             if (self.nw == 1): 
#                 self.max_heap.delete(a, self.min_heap.heap[-1]);
#                 self.min_heap.heap.pop();
#                 self.min_heap.size -= 1;
#                 if (self.min_heap.size == self.max_heap.size): self.nw = 2;
#                 else: self.nw = 1;
#             else: 
#                 self.max_heap.delete(a, self.max_heap.heap[-1]);
#                 self.max_heap.heap.pop();
#                 self.max_heap.size -= 1;
#                 if (not self.isLeft(self.max_heap.size)): self.nw = 1;
#                 else: self.nw = 2;
#         del self.mp[a];

# if __name__ == "__main__": 
#     deap = Deap();

#     num = [5, 35, 12, 21, 30, 32, 18, 16, 25, 27, 22, 29];
#     for i in num: deap.insert(i);

#     print(deap.min_heap.heap);
#     print(deap.max_heap.heap);
#     print();

#     deap.delete(29);
#     print(deap.min_heap.heap);
#     print(deap.max_heap.heap);
#     print();

#     deap.delete(21);
#     print(deap.min_heap.heap);
#     print(deap.max_heap.heap);
#     print();

#     deap.delete(12);
#     print(deap.min_heap.heap);
#     print(deap.max_heap.heap);
#     print();

#     deap.insert(40);
#     print(deap.min_heap.heap);
#     print(deap.max_heap.heap);
#     print(); 

#     deap.insert(29);
#     print(deap.min_heap.heap);
#     print(deap.max_heap.heap);
#     print(); 