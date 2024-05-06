import random
class Node: 
    def __init__(self, k) -> None:
        self.val = k
        self.pri = random.randint(0, 5201314)
        self.lch = None
        self.rch = None
        self.size = 1
    
    def pull (self): 
        self.size = 1
        if (self.lch): self.size += self.lch.size
        if (self.rch): self.size += self.rch.size

def size (p): return 0 if not p else p.size

def merge (a, b): 
    if (a is None): return b
    if (b is None): return a
    if (a.pri < b.pri): 
        a.rch = merge(a.rch, b)
        a.pull()
        return a
    else: 
        b.lch = merge(a, b.lch)
        b.pull()
        return b

def split (p, k): 
    if (p is None): return None, None
    if (p.val < k): 
        a, b = split(p.rch, k)
        p.rch = a
        p.pull()
        return p, b
    else: 
        a, b = split(p.lch, k)
        p.lch = b
        p.pull()
        return a, p

def split_by_size (p, k): 
    if (p is None): return None, None
    if (size(p.lch) < k): 
        a, b = split_by_size(p.rch, k - size(p.lch) - 1)
        p.rch = a
        p.pull()
        return p, b
    else: 
        a, b = split_by_size(p.lch, k)
        p.lch = b
        p.pull()
        return a, p

def insert (p, k): 
    if (p is None): return Node(k)
    a, b = split(p, k)
    p = merge(a, merge(Node(k), b))
    return p

def delete (p, k): 
    a, b = split(p, k)
    b, c = split(p, k + 1)
    p = merge(a, c)
    return p

def Print(p, c=""): 
    if (p != None): 
        Print(p.lch, c + 'L')
        print(p.val, c)
        Print(p.rch, c + 'R')

def modify (p, a, b): 
    p = delete(p, a)
    p = insert(p, b)
    return p

tree = None

num = [8, 2, 0, 6, 4]


nums = sorted(num)

print(nums)
print()
for i in nums: 
    if (tree == None): tree = Node(i)
    else: tree = insert(tree, i)

Print(tree)
print()


tree = insert(tree, 3)
Print(tree)
print()
tree = delete(tree, 2)
Print(tree)

print()
tree = modify(tree, 6, 7)
Print(tree)
print()
