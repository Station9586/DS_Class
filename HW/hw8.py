class MinHeap:
    def __init__(self):
        self.heap_tree = [0]  # 補0
        self.last_index = 0

    def insert(self, id_temp):
        #將數字放入min_heap
        self.last_index += 1;
        self.heap_tree.append(id_temp);
        self.adjust_up(self.last_index);

    def adjust_up(self, last_index):
        #從下往上調整
        while (last_index > 1): 
            if (self.heap_tree[last_index] >= self.heap_tree[last_index >> 1]): break;
            else: self.exchange(last_index, last_index >> 1);
            last_index >>= 1;

    def exchange(self, id1, id2):
        #交換
        self.heap_tree[id1], self.heap_tree[id2] = self.heap_tree[id2], self.heap_tree[id1];

    def adjust_down(self, index1, index2):
        #從上往下調整
        # tmp = self.heap_tree[index1];
        # idx = index1 << 1;
        # while (idx <= index2): 
        #     if (idx < index2 and self.heap_tree[idx] > self.heap_tree[idx + 1]): idx += 1;
        #     if (tmp <= self.heap_tree[idx]): break;
        #     else: 
        #         self.heap_tree[idx >> 1] = self.heap_tree[idx];
        #         idx <<= 1;
        # self.heap_tree[idx >> 1] = tmp;
        while (index1 << 1 <= index2): 
            j = index1 << 1;
            if (index1 << 1 < index2 and self.heap_tree[index1 << 1 | 1] < self.heap_tree[index1 << 1]): j += 1;
            if (self.heap_tree[j] < self.heap_tree[index1]): self.exchange(j, index1);
            index1 = j;

    def pop(self):
        #把最小值取出
        ret = self.heap_tree[1];
        self.heap_tree[1] = self.heap_tree[self.last_index];
        self.heap_tree.pop();
        self.last_index -= 1;
        if (self.last_index > 1): self.adjust_down(1, self.last_index);
        return ret;

    def find_Nth_smallest(self, n):
        #找第n小的值
        tmp = [];
        for i in range(n): tmp.append(self.pop());
        ret = tmp[-1];
        while (len(tmp)): self.insert(tmp.pop());
        return ret;


def main():

    min_heap = MinHeap()
    numbers = [15, 62, 1, 94, 11, 10, 6, 2, 57]
    numbers = [20, 1, 19, 3, 77, 46, 5, 89, 290, 104, 35, 28];
    for number in numbers:
        min_heap.insert(number)
    # print(min_heap.heap_tree)

    # print(min_heap.find_Nth_smallest(3))
    # print(min_heap.find_Nth_smallest(4))
    # print(min_heap.find_Nth_smallest(7))
    # print(min_heap.find_Nth_smallest(11))
    print(sorted(numbers, reverse=False))
    for i in range(1, len(numbers) + 1): print(f"{i}: {min_heap.find_Nth_smallest(i)}");
main()
