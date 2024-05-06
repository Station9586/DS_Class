import sys


class TreeNode:
    def __init__(self, name, score):
        self.name = name;
        self.score = score;
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert_node(self, root, name, score):
        # Standard BST insertion -> Find the correct position
        if not root: return TreeNode(name, score);
        elif score < root.score: root.left = self.insert_node(root.left, name, score);
        else: root.right = self.insert_node(root.right, name, score);

        # Update height & get balance of the ancestor Node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right));
        balanceFactor = self.getBalance(root);

        # Unbalanced -> 4 cases
        if balanceFactor > 1: 
            if score < root.left.score: return self.rightRotate(root); # LL type
            else: # LR type
                root.left = self.leftRotate(root.left);
                return self.rightRotate(root);

        if balanceFactor < -1:
            if score > root.right.score: return self.leftRotate(root); # RR type
            else: # RL type
                root.right = self.rightRotate(root.right);
                return self.leftRotate(root);

        return root

    # Function to delete a node
    def delete_node(self, root, score):
        # Standard BST deletion -> Find the correct position
        if not root: return root;
        elif score < root.score: root.left = self.delete_node(root.left, score);
        elif score > root.score: root.right = self.delete_node(root.right, score);
        else:
            if root.left is None: return root.right; # Node with only one child
            elif root.right is None: return root.right;
            else: # Node with two child
                tmp = self.getMinValueNode(root.right); # find the smallest in the right child
                root.score = tmp.score; # copy this Node
                root.name = tmp.name;
                root.right = self.delete_node(root.right, tmp.score); # delete the inorder tmp

        if root is None: return root; # if tree have only one Node -> return

        # Update height & get balance
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right));
        balanceFactor = self.getBalance(root);

        # Unbalanced -> 4 cases
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0: return self.rightRotate(root); # LL type
            else: # LR type
                root.left = self.leftRotate(root.left);
                return self.rightRotate(root);
        elif balanceFactor < -1:
            if self.getBalance(root.right) <= 0: return self.leftRotate(root); # RR type
            else: # RL type
                root.right = self.rightRotate(root.right);
                return self.leftRotate(root);

        return root;

    def search_node(self, root, name, score):
        current = root
        while current != None and score != current.score and name != current.name:
            if score < current.score:
                current = current.left
            else:
                current = current.right

        return current

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factor of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def inorder(self, root):
        if (root): 
            self.inorder(root.left);
            print(f"{root.name} {root.score}");
            self.inorder(root.right);

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.score)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)


myTree = AVLTree()
root = None

names = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [33, 13, 52, 9, 21, 61, 8, 11]

for name, num in zip(names, nums):
    root = myTree.insert_node(root, name, num)

current = myTree.search_node(root, "d", 9)
print(f"{current.name} {current.score}", end="\n\n")

myTree.printHelper(root, "", True)
score = 13
root = myTree.delete_node(root, score)
print("After Deletion: ")
myTree.printHelper(root, "", True)

print()
print("Display inorder output :")
myTree.inorder(root);
