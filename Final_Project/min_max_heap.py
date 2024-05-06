class MinMaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def delete_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        self._swap(0, len(self.heap) - 1)
        min_value = self.heap.pop()
        self._sift_down(0)
        return min_value

    def delete_max(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        max_index = self._get_max_index()
        self._swap(max_index, len(self.heap) - 1)
        max_value = self.heap.pop()
        self._sift_down(max_index)
        return max_value

    def _sift_up(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            self._sift_up(parent_index)
        elif self.heap[index] > self.heap[parent_index]:
            grandparent_index = (parent_index - 1) // 2
            if self.heap[index] > self.heap[grandparent_index]:
                self._swap(index, grandparent_index)
                self._sift_up(grandparent_index)

    def _sift_down(self, index):
        if index >= len(self.heap):
            return
        min_child_index = self._get_min_child_index(index)
        max_child_index = self._get_max_child_index(index)
        if min_child_index is not None and self.heap[index] > self.heap[min_child_index]:
            self._swap(index, min_child_index)
            self._sift_down(min_child_index)
        elif max_child_index is not None and self.heap[index] < self.heap[max_child_index]:
            self._swap(index, max_child_index)
            self._sift_down(max_child_index)

    def _get_min_child_index(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        if left_child_index >= len(self.heap):
            return None
        elif right_child_index >= len(self.heap):
            return left_child_index
        else:
            return left_child_index if self.heap[left_child_index] < self.heap[right_child_index] else right_child_index

    def _get_max_child_index(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        if left_child_index >= len(self.heap):
            return None
        elif right_child_index >= len(self.heap):
            return left_child_index
        else:
            return left_child_index if self.heap[left_child_index] > self.heap[right_child_index] else right_child_index

    def _get_max_index(self):
        if len(self.heap) == 1:
            return 0
        max_index = 1 if self.heap[1] > self.heap[2] else 2
        return max_index if self.heap[max_index] > self.heap[0] else 0

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
