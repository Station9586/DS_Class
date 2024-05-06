class Node: 
    def __init__ (self, a) -> None: 
        self.val = a
        self.lch = None
        self.rch = None
        self.par = None

class BinarySearchTree: 
    def __init__ (self, root = None) -> None: 
        self.root = root

    def search (self, a) -> Node: 
        cur = self.root
        while (cur): 
            if (a == cur.val): return cur
            elif (a < cur.val): cur = cur.lch
            else: cur = cur.rch
        return cur

    def insert (self, a) -> None: 
        if (self.root is None): 
            self.root = Node(a)
            return
        cur = self.root
        nw = Node(a)
        while (True): 
            if (cur.val > nw.val): 
                if (cur.lch): cur = cur.lch
                else: 
                    nw.par = cur
                    cur.lch = nw
                    break
            elif (cur.val < nw.val): 
                if (cur.rch): cur = cur.rch
                else: 
                    nw.par = cur
                    cur.rch = nw
                    break

    def getMx (self) -> Node: 
        cur = self.root
        while (cur.rch): cur = cur.rch
        return cur

    def delete (self, a) -> None: 
        d = self.search(a)
        par = d.par
        if (not d.lch and not d.rch): 
            if (par): 
                if (par.lch == d): par.lch = None
                else: par.rch = None
            else: self.root = None
            return
        if (not d.lch and d.rch): 
            if (par): 
                if (par.lch == d): par.lch = d.rch
                else: par.rch = d.rch
            else: self.root = d.rch
            return
        if (d.lch): 
            lch = BinarySearchTree(d.lch)
            mx = lch.getMx()
            if (mx == d.lch):  
                mx.rch = d.rch
                mx.par = d.par
                if (not par): self.root = mx
                return
            if (mx.lch): mx.par.rch = mx.lch
            else: mx.par.rch = None
            if (par): 
                if (par.lch == d): par.lch = mx
                else: par.rch = mx
            else: self.root = mx
            mx.lch = d.lch
            mx.rch = d.rch
            return

    def Print (self, p: Node, c = "") -> None:
        if (p != None): 
            self.Print(p.lch, c + "L")
            print(p.val, c)
            self.Print(p.rch, c + "R")