from Que_Stk import Queue, Stack
from PriorityQueue import MinHeap

class Node: 
    def __init__ (self, data, val) -> None: 
        self.v = data
        self.val = val # weight
    
    def __lt__ (self, other): return self.val < other.val

    def __ge__ (self, other): return self.val >= other.val


def Topological_Sort (gp, In): # data: Graph, In: In-degree
    q = Queue()
    n = len(gp)
    for i in range(1, n + 1): 
        if (In[i] == 0): q.push(i)
    
    ret = []
    while (not q.empty()): 
        u = q.front()
        ret.append(u)
        q.pop()
        for i in gp[u]: 
            In[i] -= 1
            if (In[i] == 0): q.push(i)
    
    return ret

def Kruskal_algo (data, n, m): # using disjoint set, n: number of nodes, data is a class that contains (u, v, w), m: number of edges
    p = [i for i in range(n + 1)]

    def find (x): 
        if (p[x] == x): return x
        p[x] = find(p[x])
        return p[x]

    def Union (a, b): 
        p[find(a)] = find(b)

    data.sort(key = lambda x: x.w)
    ret = 0
    j = 1
    i = 0
    while (i < m and j <= n): 
        if (find(data[i].u) != find(data[i].v)): 
            Union(data[i].u, data[i].v)
            ret += data[i].w
            j += 1
        i += 1
    if (j != n): return -1
    return ret

def Dijkstra_algo (data, n): # data is a class that contains (v, w), n: number of nodes
    d = [1e9 for _ in range(n + 1)]
    d[1] = 0

    pq = MinHeap()
    pq.insert(Node(1, 0))

    while (pq.size): 
        now = pq.pop().v;
        for node in data[now]: 
            i = node.v; w = node.val;
            if (d[i] > d[now] + w): 
                d[i] = d[now] + w
                pq.insert(Node(i, d[i]))
    
    return d

def SCC (gp, rev, n): # gp: graph, rev: reverse graph, n: number of nodes
    # turn graph into DAG
    vis = [False for _ in range(n + 1)]
    scc = [0 for _ in range(n + 1)]
    sccid = 0
    stk = Stack()
    def dfs1 (now): 
        vis[now] = 1
        for i in gp[now]: 
            if (not vis[i]): dfs1(i)
        stk.push(now)

    def dfs2 (now): 
        vis[now] = 1
        scc[now] = sccid
        for i in rev[now]: 
            if (not vis[i]): dfs2(i)

    for i in range(1, n + 1): 
        if (not vis[i]): dfs1(i)
    vis = [False for _ in range(n + 1)]

    while (not stk.empty()):
        u = stk.top()
        stk.pop()
        if (vis[u]): continue
        sccid += 1
        dfs2(u)

    new_gp = [[] for _ in range(sccid + 1)]

    for i in range(1, n + 1): 
        for j in gp[i]: 
            if (scc[i] != scc[j]): new_gp[scc[i]].append(scc[j])

    return new_gp

def Maximum_Flow (gp, n, m): 
    parent = [0 for _ in range(n + 1)]
    def bfs (): 
        vis = [0] * (n + 1)
        q = Queue()
        q.push(1)
        while (not q.empty()): 
            now = q.front()
            q.pop()
            for i in range(1, n + 1): 
                if (gp[now][i] > 0 and not vis[i]): 
                    q.push(i)
                    vis[i] = True
                    parent[i] = now

        return vis[n]

    ret = 0
    while (bfs()): 
        flow = 1e18
        i = n
        while (i != 1): 
            i = parent[i]
            flow = min(flow, gp[parent[i]][i])
        ret += flow
        i = n
        while (i != 1): 
            i = parent[i]
            gp[parent[i]][i] -= flow
            gp[i][parent[i]] += flow

    return ret
