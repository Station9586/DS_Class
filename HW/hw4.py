class Stack: 
    def __init__ (self): 
        self.stk = [];
        self.size = 0;

    def push (self, a): 
        self.stk.append(a);
        self.size += 1;

    def top (self): return self.stk[-1];

    def empty (self): return self.size == 0;

    def pop (self): 
        self.stk.pop();
        self.size -= 1;

class Node: 
    def __init__ (self, x, y): 
        self.x = x;
        self.y = y;

    def val (self): return self.x, self.y;

def Print (pos): 
    pos.reverse();
    for a, b in pos: print(f"({a},{b})=>");

def Retrace (par, n, m) -> list: 
    ans = [];
    i = n - 1;
    j = m - 1;
    while (i != 0 or j != 0): 
        ans.append([par[i][j].x, par[i][j].y]);
        i, j = par[i][j].val();
    return ans;

def isValid (a, b, maze) -> bool: 
    n = len(maze);
    m = len(maze[0]);
    return 0 <= a and a < n and 0 <= b and b < m and (maze[a][b] == 0);

dx = [1, 0, -1, 0];
dy = [0, 1, 0, -1];

def maze_solver(maze):
    #請在此作答
    if (maze[0][0] == 1): return 0;
    n = len(maze);
    m = len(maze[0]);
    prev = [[Node(0, 0) for _ in range(m)] for _ in range(n)];
    stk = Stack();
    stk.push([0, 0]);
    global dx, dy;
    while (not stk.empty()): 
        x, y = stk.top();
        maze[x][y] = 2;
        if (x == n - 1 and y == m - 1):
            ans = Retrace(prev, n, m);
            Print(ans);
            return 1;
        find = 0;
        for i in range(4): 
            nx = x + dx[i];
            ny = y + dy[i];
            if (isValid(nx, ny, maze)): 
                prev[nx][ny] = Node(x, y);
                stk.push([nx, ny]);
                find = 1;
                break;
        if (not find): 
            x, y = prev[x][y].val();
            stk.pop();

    return 0;
    
def maze_solver2(maze):
    #請在此作答
    n = len(maze);
    m = len(maze[0]);
    prev = [[Node(0, 0) for _ in range(m)] for _ in range(n)];
    stk = Stack();
    stk.push([0, 0]);
    while (not stk.empty()): 
        x, y = stk.top();
        maze[x][y] = 2;
        if (x == n - 1 and y == m - 1): 
            ans = Retrace(prev, n, m);
            Print(ans);
            return 1;
        if (y < m - 1 and maze[x][y + 1] == 0): 
            prev[x][y + 1] = Node(x, y);
            y += 1;
            stk.push([x, y]);
        elif (x < n - 1 and maze[x + 1][y] == 0): 
            prev[x + 1][y] = Node(x, y);
            x += 1;
            stk.push([x, y]);
        elif (y > 0 and maze[x][y - 1] == 0): 
            prev[x][y - 1] = Node(x, y);
            y -= 1;
            stk.push([x, y]);
        elif (x > 0 and maze[x - 1][y] == 0): 
            prev[x - 1][y] = Node(x, y);
            x -= 1;
            stk.push([x, y]);
        else: 
            x, y = prev[x][y].val();
            stk.pop();
    return 0;



##############此區塊請勿更動################

def main():
    maze = [[0, 1, 1, 0],
            [0, 0, 1, 0],
            [1, 0, 1, 0],
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 0]];

    maze2 = [[0, 1, 0, 0],
             [0, 0, 1, 0],
             [1, 0, 0, 1],
             [0, 1, 0, 0]]

    maze3 = [[1, 1, 0, 0, 1, 0],
             [0, 0, 1, 0, 0, 1],
             [1, 0, 0, 1, 0, 1],
             [0, 1, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 1, 0]];

    maze4 = [[0, 1, 1, 0, 1],
             [0, 0, 1, 0, 0],
             [1, 0, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 1, 1, 0],
             [1, 1, 0, 0, 0]];

    print("通往終點的路徑:")
    if maze_solver(maze):
        print("(%d,%d)" % (len(maze) - 1, len(maze[0]) - 1))
    else:
        print("沒有通往終點的路徑")

    print("\n通往終點的路徑:")
    if maze_solver(maze2):
        print("(%d,%d)" % (len(maze2) - 1, len(maze2[0]) - 1))
    else:
        print("沒有通往終點的路徑")

    print("\n通往終點的路徑:")
    if maze_solver(maze3):
        print("(%d,%d)" % (len(maze3) - 1, len(maze3[0]) - 1))
    else:
        print("沒有通往終點的路徑")

    print("\n通往終點的路徑:")
    if maze_solver(maze4):
        print("(%d,%d)" % (len(maze4) - 1, len(maze4[0]) - 1))
    else:
        print("沒有通往終點的路徑")
main()
##############此區塊請勿更動################