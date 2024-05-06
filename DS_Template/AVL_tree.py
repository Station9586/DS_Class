class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root: return Node(key)
        elif key < root.key: root.left = self._insert(root.left, key)
        else: root.right = self._insert(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1:
            if key < root.left.key: return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
        elif balance < -1:
            if key > root.right.key: return self._rotate_left(root)
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root: return root
        elif key < root.key: root.left = self._delete(root.left, key)
        elif key > root.key: root.right = self._delete(root.right, key)
        else:
            if not root.left: return root.right
            elif not root.right: return root.left
            else:
                successor = self._get_min_value_node(root.right)
                root.key = successor.key
                root.right = self._delete(root.right, successor.key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1:
            if self._get_balance(root.left) >= 0: return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
        elif balance < -1:
            if self._get_balance(root.right) <= 0: return self._rotate_left(root)
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        return root

    def modify(self, old_key, new_key):
        self.delete(old_key)
        self.insert(new_key)

    def _get_height(self, root):
        if not root: return 0
        return root.height

    def _get_balance(self, root):
        if not root: return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_min_value_node(self, root):
        current = root
        while current.left: current = current.left
        return current

    def inorder(self):
        self._inorder(self.root)
    
    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.key, end = " ")
            self._inorder(root.right)