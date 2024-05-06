class Node: 
    def __init__(self, data) -> None:
        self.data = data;
        self.nxt = None;

class Queue: 
    def __init__(self) -> None:
        self.head = None;
        self.tail = None;
    
    def __len__ (self) -> int: 
        ret = 0;
        cur = self.head;
        while (cur != None): 
            ret += 1;
            cur = cur.nxt;
        return ret;
    
    def push (self, data) -> None: 
        nw = Node(data);
        if (self.head == None): 
            self.head = nw;
            self.tail = nw;
        else: 
            self.tail.nxt = nw;
            self.tail = self.tail.nxt;
    
    def pop (self) -> None: 
        if (len(self) == 1): 
            self.head = None;
            self.tail = None;
        else: self.head = self.head.nxt;
    
    def front (self): return self.head.data; 

    def empty (self) -> bool: return self.head == None;

def Count_RiceField(gp):
    n = len(gp);
    m = len(gp[0]);

    ans = 0;
    vis = [[0] * m for _ in range(n)];

    dx = [1, 0, -1, 0];
    dy = [0, 1, 0, -1];

    def bfs (i: int, j: int) -> None: 
        q = Queue();
        q.push((i, j));
        vis[i][j] = 1;
        while (not q.empty()): 
            x, y = q.front();
            q.pop();
            for k in range(4): 
                nx = x + dx[k];
                ny = y + dy[k];
                if (nx >= 0 and nx < n and ny >= 0 and ny < m and gp[nx][ny] == "1" and not vis[nx][ny]): 
                    q.push((nx, ny));
                    vis[nx][ny] = 1;

    for i in range(n):
        for j in range(m):
            if (gp[i][j] == "1" and not vis[i][j]):
                bfs(i, j);
                ans += 1;

    print(ans);


def main():
    map = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "0", "1", "0"],
        ["0", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]

    Count_RiceField(map)

main()
