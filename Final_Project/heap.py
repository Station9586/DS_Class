class MinHeap: 
    def __init__ (self) -> None: 
        self.heap = [-1];
        self.size = 0;

    def swap (self, a, b) -> None: self.heap[a], self.heap[b] = self.heap[b], self.heap[a];

    def swim (self, n) -> None: 
        while (n): 
            if (self.heap[n] >= self.heap[n >> 1]): break;
            else: self.swap(n, n >> 1);
            n >>= 1;

    def insert (self, data) -> None: 
        self.heap.append(data);
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
        if (self.size > 1): self.push(1, self.size);
        return ret;

    def kth (self, n) -> int: 
        tmp = [];
        for _ in range(n): tmp.append(self.pop());
        ret = tmp[-1];
        while (len(tmp)): self.insert(tmp.pop());
        return ret;

# a = MinHeap();
# numbers = [20, 1, 19, 3, 77, 46, 5, 89, 290, 104, 35, 28];

# print(sorted(numbers));
# for i in numbers: a.insert(i);
# for i in range(1, len(numbers) + 1): print(f"{i}: {a.kth(i)}");