#####################請在本區域作答#####################
# 第一題回答區-----
# 1-1
# 1-2
# 第二題回答區-----
class Node:
    def __init__ (self, key): 
        self.key1 = key;
        self.key2 = None;
        self.left = None;
        self.middle = None;
        self.right = None;

    def isLeaf (self): return self.left is None and self.middle is None and self.right is None;

    def isFull (self): return self.key2 is not None;

    def hasKey (self, key): 
        if (self.key1 == key or (self.isFull() and self.key2 == key)): return True;
        return False;

    def getChild (self, key): 
        if (key < self.key1): return self.left;
        elif (self.key2 is None or key < self.key2): return self.middle;
        return self.right;

class TwoThreeTree:
    def __init__ (self): 
        self.root = None;

    def split (self, node, key, pRef): 
        nw = Node(None);
        if (key < node.key1): 
            pKey = node.key1;
            node.key1 = key;
            nw.key1 = node.key2;
            if (pRef is not None): 
                nw.left = node.middle;
                nw.middle = node.right;
                node.middle = pRef;
        elif (key < node.key2): 
            pKey = key;
            nw.key1 = node.key2;
            if (pRef is not None): 
                nw.left = pRef;
                nw.middle = node.right;
        else: 
            pKey = node.key2;
            nw.key1 = key;
            if (pRef is not None): 
                nw.left = node.right;
                nw.middle = pRef;
        node.key2 = None;
        node.right = None;
        return pKey, nw;

    def addToNode (self, node, key, pRef): 
        if (node.isFull()): return self.split(node, key, pRef);
        else: 
            if (key < node.key1): 
                node.key2 = node.key1;
                node.key1 = key;
                if (pRef is not None): 
                    node.right = node.middle;
                    node.middle = pRef;
            else: 
                node.key2 = key;
                if (pRef is not None): node.right = pRef;
            return None, None;

    def put (self, node, key): 
        if (node.hasKey(key)): return None, None;
        elif (node.isLeaf()): return self.addToNode(node, key, None);
        else: 
            child = node.getChild(key);
            pKey, pRef = self.put(child, key);
            if (pKey is None): return None, None;
            return self.addToNode(node, pKey, pRef);

    def insert (self, key): 
        if (self.root is None): 
            self.root = Node(key);
            return;
        pKey, pRef = self.put(self.root, key);
        if (pKey is not None): 
            nw = Node(pKey);
            nw.left = self.root;
            nw.middle = pRef;
            self.root = nw;

    def reverse (self, node): 
        if (node.left != None): self.reverse(node.left);
        if (node.middle != None): self.reverse(node.middle);
        if (node.right != None): self.reverse(node.right);

        if (node.isFull()): node.key1, node.key2 = node.key2, node.key1;
        # else: 
        #     node.key2 = node.key1;
        #     node.key1 = None;

        if (node.left != None and node.middle != None and node.right != None): node.left, node.right = node.right, node.left;
        elif (node.left != None and node.middle != None): node.left, node.middle = node.middle, node.left;
        # elif (node.left != None): 
        #     node.right = node.left;
        #     node.left = None;

    def show_f (self, node, c = "") -> None: 
        print(node.key1, end = "");
        if (node.key2 != None): print(",", node.key2, c);
        else: print("", c);
        if (node.left != None): self.show_f(node.left, c + "L");
        if (node.middle != None): self.show_f(node.middle, c + "M");
        if (node.right != None): self.show_f(node.right, c + "R");
#####################請在本區域作答#####################

######測試區######
# tree = TwoThreeTree()
# tree.insert(60)
# tree.insert(35)
# # tree.insert(80)
# # tree.insert(15)
# # tree.insert(10)
# tree.show_f(tree.root)

# print();
# tree.reverse(tree.root);
# tree.show_f(tree.root);
# print();

tree = TwoThreeTree();
num = [45, 30, 10, 20, 40, 70, 50, 80, 85, 60, 90]
a = [53, 11, 32, 77, 64];
b = [19, 25, 38, 43, 52, 64, 87];
c = [5, 2, 6, 9, 4, 7, 1];

print("Initial: ");
for i in num: tree.insert(i);
tree.show_f(tree.root);
print();

print("Reverse: ");
tree.reverse(tree.root);
tree.show_f(tree.root);
print();

# tree.reverse(tree.root.left);
# tree.show_f(tree.root);
# print();

# print("Insert a:");
# for i in a: tree.insert(i);
# tree.show_f(tree.root);
# print();

# print("Insert b:");
# for i in b: tree.insert(i);
# tree.show_f(tree.root);
# print();

# print("Insert c: ");
# for i in c: tree.insert(i);


# # tree.insert(55);
# tree.show_f(tree.root);
# print();

# print("Reverse 2:");
# tree.reverse(tree.root);
# tree.show_f(tree.root);
# print();
# ######測試區######