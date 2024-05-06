# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#         self.height = 1

# class AVLTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, key):
#         self.root = self._insert(self.root, key)

#     def _insert(self, root, key):
#         if not root: return Node(key)
#         elif key < root.key: root.left = self._insert(root.left, key)
#         else: root.right = self._insert(root.right, key)

#         root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

#         balance = self._get_balance(root)

#         if balance > 1:
#             if key < root.left.key: return self._rotate_right(root)
#             else:
#                 root.left = self._rotate_left(root.left)
#                 return self._rotate_right(root)
#         elif balance < -1:
#             if key > root.right.key: return self._rotate_left(root)
#             else:
#                 root.right = self._rotate_right(root.right)
#                 return self._rotate_left(root)

#         return root

#     def delete(self, key):
#         self.root = self._delete(self.root, key)

#     def _delete(self, root, key):
#         if not root: return root
#         elif key < root.key: root.left = self._delete(root.left, key)
#         elif key > root.key: root.right = self._delete(root.right, key)
#         else:
#             if not root.left: return root.right
#             elif not root.right: return root.left
#             else:
#                 successor = self._get_min_value_node(root.right)
#                 root.key = successor.key
#                 root.right = self._delete(root.right, successor.key)

#         root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

#         balance = self._get_balance(root)

#         if balance > 1:
#             if self._get_balance(root.left) >= 0: return self._rotate_right(root)
#             else:
#                 root.left = self._rotate_left(root.left)
#                 return self._rotate_right(root)
#         elif balance < -1:
#             if self._get_balance(root.right) <= 0: return self._rotate_left(root)
#             else:
#                 root.right = self._rotate_right(root.right)
#                 return self._rotate_left(root)

#         return root

#     def modify(self, old_key, new_key):
#         self.delete(old_key)
#         self.insert(new_key)

#     def _get_height(self, root):
#         if not root: return 0
#         return root.height

#     def _get_balance(self, root):
#         if not root: return 0
#         return self._get_height(root.left) - self._get_height(root.right)

#     def _rotate_left(self, z):
#         y = z.right
#         T2 = y.left

#         y.left = z
#         z.right = T2

#         z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
#         y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

#         return y

#     def _rotate_right(self, z):
#         y = z.left
#         T3 = y.right

#         y.right = z
#         z.left = T3

#         z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
#         y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

#         return y

#     def _get_min_value_node(self, root):
#         current = root
#         while current.left: current = current.left
#         return current

#     def inorder(self):
#         self._inorder(self.root);
    
#     def _inorder(self, root):
#         if root:
#             self._inorder(root.left)
#             print(root.key, end = " ")
#             self._inorder(root.right)
    
class TreeNode:
    def __init__(self, course, score):
        self.course = course;
        self.score = score;
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self): self.root = None

    def insert_node(self, root, course, score):
        # Standard BST insertion -> Find the correct position
        if not root: return TreeNode(course, score);
        elif score < root.score: root.left = self.insert_node(root.left, course, score);
        else: root.right = self.insert_node(root.right, course, score);

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
            if score >= root.right.score: return self.leftRotate(root); # RR type
            else: # RL type
                root.right = self.rightRotate(root.right);
                return self.leftRotate(root);

        return root

    # Function to delete a node
    def delete_node(self, root, score, course):
        # Standard BST deletion -> Find the correct position
        if not root: return root;
        elif score < root.score: root.left = self.delete_node(root.left, score, course);
        elif score >= root.score and course != root.course: root.right = self.delete_node(root.right, score, course);
        else:
            if root.left is None: return root.right; # Node with only one child
            elif root.right is None: return root.right;
            else: # Node with two child
                tmp = self.getMinValueNode(root.right); # find the smallest in the right child
                root.score = tmp.score; # copy this Node
                root.course = tmp.course;
                root.right = self.delete_node(root.right, tmp.score, tmp.course); # delete the inorder tmp

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

    def search_node(self, root, course, score):
        current = root
        while current != None and score != current.score and course != current.course:
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

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def inorder(self, root):
        if (self.root == None): 
            print("Empty Score.");
            return;
        if (root): 
            self.inorder(root.left);
            print(f"{root.course}: {root.score}");
            self.inorder(root.right);

    def search_course (self, root, course): 
        if (root): 
            self.search_course(root.left, course);
            if (root.course == course): 
                # print(f"Score is already exists.");
                return True;
            self.search_course(root.right, course);
        return False;