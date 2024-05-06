# Segment tree with lazy propagation (Range sum Version)
class SegmentTree:
    def __init__(self, arr) -> None:
        self.val = [0] * (4 * len(arr))
        self.tag = [0] * (4 * len(arr))  # add
        self.set_tag = [0] * (4 * len(arr))  # set
        self.build(arr, 1, 0, len(arr) - 1)

    def pull (self, node) -> None: 
        self.val[node] = self.val[node << 1] + self.val[node << 1 | 1]

    def build(self, arr, node, L, R) -> None:
        if (L == R):
            self.val[node] = arr[L]
            return
        mid = (L + R) >> 1
        self.build(arr, node << 1, L, mid)
        self.build(arr, node << 1 | 1, mid + 1, R)
        self.pull(node)
        # self.val[node] = self.val[node << 1] + self.val[node << 1 | 1]

    def apply(self, node, L, R, x) -> None:  # add
        self.tag[node] += x
        self.val[node] += x * (R - L + 1)

    def apply_set(self, node, L, R, x) -> None:  # set
        self.set_tag[node] = x
        self.val[node] = x * (R - L + 1)
        self.tag[node] = 0

    def push(self, node, L, R) -> None:
        mid = (L + R) >> 1
        if (L == R): return
        if (self.set_tag[node] != 0):
            self.apply_set(node << 1, L, mid, self.set_tag[node])
            self.apply_set(node << 1 | 1, mid + 1, R, self.set_tag[node])
            self.set_tag[node] = 0

        if (self.tag[node] != 0):
            self.apply(node << 1, L, mid, self.tag[node])
            self.apply(node << 1 | 1, mid + 1, R, self.tag[node])
            self.tag[node] = 0

    def modify(self, node, L, R, l, r, x) -> None:  # add
        if (l > R or r < L): return
        if (l <= L and R <= r):
            self.apply(node, L, R, x)
            return
        self.push(node, L, R)
        mid = (L + R) >> 1
        self.modify(node << 1, L, mid, l, r, x)
        self.modify(node << 1 | 1, mid + 1, R, l, r, x)
        self.pull(node)
        # self.val[node] = self.val[node << 1] + self.val[node << 1 | 1]

    def update(self, node, L, R, l, r, x) -> None:  # set
        if (l > R or r < L): return
        if (l <= L and R <= r):
            self.apply_set(node, L, R, x)
            return
        self.push(node, L, R)
        mid = (L + R) >> 1
        self.update(node << 1, L, mid, l, r, x)
        self.update(node << 1 | 1, mid + 1, R, l, r, x)
        self.pull(node)
        # self.val[node] = self.val[node << 1] + self.val[node << 1 | 1]

    def query(self, node, L, R, l, r) -> int:
        if (l > R or r < L): return 0
        if (l <= L and R <= r): return self.val[node]
        self.push(node, L, R)
        mid = (L + R) >> 1
        return self.query(node << 1, L, mid, l, r) + self.query(node << 1 | 1, mid + 1, R, l, r)

# Binary Indexed Tree 樹狀數組
def lowbit (x: int) -> int: 
    return x & (-x)

class BIT: 
    def __init__(self, n: int) -> None:
        self.sz = n
        self.bit = [0] * (n + 1)

    def query (self, x: int) -> int: 
        sum = 0
        while (x): 
            sum += self.bit[x]
            x -= lowbit(x)
        return sum
    
    def update (self, x: int, val: int) -> None: 
        while (x <= self.sz): 
            self.bit[x] += val
            x += lowbit(x)

    def modify (self, x: int, val: int) -> None: 
        self.bit[x] = 0
        while (x <= self.sz): 
            self.bit[x] += val
            x += lowbit(x)