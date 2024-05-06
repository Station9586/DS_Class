import sys

class Node: 
    def __init__(self, v, w) -> None:
        self.v = v
        self.w = w

class MinHeap: 
    def __init__ (self) -> None: 
        self.heap = [Node(-1, -1)]
        self.size = 0

    def swap (self, a, b) -> None: self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def swim (self, n) -> None: 
        while (n): 
            if (self.heap[n].w >= self.heap[n >> 1].w): break
            else: self.swap(n, n >> 1)
            n >>= 1

    def insert (self, data) -> None: 
        self.heap.append(data)
        self.size += 1
        self.swim(self.size)

    def push (self, i, n) -> None: 
        while (i << 1 <= n): 
            j = i << 1
            if (j < n and self.heap[j + 1].w < self.heap[j].w): j += 1
            if (self.heap[j].w < self.heap[i].w): self.swap(j, i)
            i = j

    def pop (self) -> int: 
        ret = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        if (self.size > 1): self.push(1, self.size)
        return ret

    def empty (self) -> bool: return self.size == 0

mxN = 110
gp = [[] for _ in range(mxN)]
INF = int(1e18)
dis = [INF] * mxN
par = [-1] * mxN

a = [[0] * (mxN) for _ in range(mxN)]

source = 0
sink = 0;

n = 0;

def init (): 
    global gp, a;
    try: inputStream = open("sh_path.dat", "r");
    except FileNotFoundError: print("File not found"); return;

    global n, source, sink;
    try: n = eval(inputStream.readline().strip("\n"));
    except Exception: pass;

    done = False;
    while (not done): 
        try: 
            tmp = inputStream.readline().strip("\n").split(" ");
            i = eval(tmp[0]);
            j = eval(tmp[1]);
            w = eval(tmp[2]);
        except Exception: done = True;

        gp[i].append(Node(j, w));
        a[i][j] = w;
    inputStream.close();

    # source = eval(input("Enter source: "));
    # sink = eval(input("Enter sink: "));
    source = 1;
    sink = 7;

def dijkstra ():
    global gp, dis, par, source, sink;
    pq = MinHeap(); # priority queue
    pq.insert(Node(source, 0));
    dis[source] = 0;
    while (not pq.empty()): 
        u = pq.pop();
        for i in gp[u.v]: 
            v = i.v;
            w = i.w;
            if (dis[v] > dis[u.v] + w): 
                dis[v] = dis[u.v] + w;
                par[v] = u.v;
                pq.insert(Node(v, dis[v]));

def print_path (): 
    global par, source, sink;
    n = sink;
    if (par[sink] == -1): print("No path found");
    else: 
        path = [];
        while (sink != -1): 
            path.append(sink);
            sink = par[sink];
        path.reverse();
        print(f"The shortest Path from V{source} to V{n}: ");
        print(f"V{path[0]} ", end = "");
        for i in range(1, len(path)): 
            print(f"--({a[path[i - 1]][path[i]]})--> V{path[i]}", end=" \n"[i == len(path) - 1]);
        print(f"Total length: {dis[n]}");


def main (): 
    init();
    dijkstra();
    print_path();
main();