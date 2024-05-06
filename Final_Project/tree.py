import random
class Node: 
    def __init__(self, k, name) -> None:
        self.val = k;
        self.name = name;
        self.pri = random.randint(0, 31415926);
        self.lch = None;
        self.rch = None;
        self.size = 1;
    
    def pull (self): 
        self.size = 1;
        if (self.lch): self.size += self.lch.size;
        if (self.rch): self.size += self.rch.size;

def size (p): return 0 if not p else p.size;

def merge (a, b): 
    if (a is None): return b;
    if (b is None): return a;
    if (a.pri < b.pri): 
        a.rch = merge(a.rch, b);
        a.pull();
        return a;
    else: 
        b.lch = merge(a, b.lch);
        b.pull();
        return b;

def split (p, k): 
    if (p is None): return None, None;
    if (p.val < k): 
        a, b = split(p.rch, k);
        p.rch = a;
        p.pull();
        return p, b;
    else: 
        a, b = split(p.lch, k);
        p.lch = b;
        p.pull();
        return a, p;

def split_by_size (p, k): 
    if (p is None): return None, None;
    if (size(p.lch) < k): 
        a, b = split_by_size(p.rch, k - size(p.lch) - 1);
        p.rch = a;
        p.pull();
        return p, b;
    else: 
        a, b = split_by_size(p.lch, k);
        p.lch = b;
        p.pull();
        return a, p;

def split_by_name (p, name): 
    if (p is None): return None, None;
    if (p.name < name): 
        a, b = split_by_name(p.rch, name);
        p.rch = a;
        p.pull();
        return p, b;
    else: 
        a, b = split_by_name(p.lch, name);
        p.lch = b;
        p.pull();
        return a, p;

def insert (p, k, name = ""): 
    if (p is None): return Node(k, name);
    a, b = split(p, k);
    p = merge(a, merge(Node(k, name), b));
    return p;

def delete (p, k, name = ""): 
    a, b = split(p, k);
    b, d = split(b, k + 1);
    b, c = split_by_name(b, name);
    c, e = split_by_size(c, 1);
    print(f"test: {c.val}, {c.name}");
    p = merge(a, merge(b, merge(e, d)));
    return p;

def delete2 (p, k): 
    a, b = split_by_size(p, k);
    p = b;
    return p;

def Print(p, c=""): 
    if (p != None): 
        Print(p.lch, c + 'L');
        print(p.val, c);
        Print(p.rch, c + 'R');

def modify (p, a, b): 
    p = delete(p, a);
    p = insert(p, b);
    return p;

def passed_student (p, k = 60): 
    a, b = split(p, k);
    ret = [];
    def inorder (p): 
        if (p != None): 
            inorder(p.lch);
            ret.append(p.name);
            inorder(p.rch);
    inorder(b);
    p = merge(a, b);
    return p, ret;

# tree = None;

# # num = [8, 2, 0, 6, 4];
# num = [6, 3, 7, 1, 5, 2, 4];

# num = [30, 15, 40, 33, 50, 35, 34];

# nums = sorted(num);

# print(nums);
# print();
# for i in nums: 
#     if (tree == None): tree = Node(i);
#     else: tree = insert(tree, i);

# Print(tree);
# print();


# tree = delete(tree, 40);
# Print(tree);
# print();

# # tree = insert(tree, 3);
# # Print(tree);
# # print();
# # tree = delete2(tree, 2);
# # Print(tree);

# # print();
# # tree = modify(tree, 34, 20);
# # Print(tree);
# # print();
