mxRow = 8;
mxCol = 20;
Dead = 0;
Alive = 1;
map_ = [[Dead for _ in range(mxCol)] for _ in range(mxRow)];
newMap = [[Alive for _ in range(mxCol)] for _ in range(mxRow)];
Generation = 0;

pre_map = [[1, 1], [1, 3], [1, 4], [3, 5], [3, 6], [3, 7], [4, 5], [3, 7], [5, 7], [6, 6], [6, 8], [7, 6], [7, 8]];

def init (): 
    global mxRow, mxCol, Dead, Alive, map_, newMap;
    global pre_map;
    row = 0;
    col = 0;
    print("Game of Life Program ");
    print("Enter (x, y) where (x, y) is a living cell");
    print(f"0 <= x <= {mxRow - 1}, 0 <= y <= {mxCol - 1}");
    print("Terminate with (x, y) = (-1, -1)");
    for i in pre_map: map_[i[0]][i[1]] = Alive;
    while (row != -1 and col != -1): 
        row = int(input("x-->"));
        col = int(input("y-->"));
        if (0 <= row and row < mxRow and 0 <= col and cal < mxCol): map_[row][col] = Alive;
        elif (row == -1 and col == -1): print("Input is terminated");
        else: print("(x, y) exceeds map range!");

def Neighbors (row, col): 
    global mxRow, mxCol, map_, newMap;
    cnt = 0;
    for r in range(row - 1, row + 2): 
        for c in range(col - 1, col + 2): 
            if (r < 0 or r >= mxRow or c < 0 or c >= mxCol): continue;
            if map_[r][c] == Alive: cnt += 1;

    if (map_[row][col] == Alive): cnt -= 1;
    return cnt;

def output_map (): 
    global mxRow, mxCol, map_, newMap, Generation;
    space = " ";
    print(space, "\nGame of life cell status");
    Generation += 1;
    print("------Generation %d------" % Generation);
    for row in range(mxRow): 
        print();
        print(space);
        for col in range(mxCol): 
            if (map_[row][col] == Alive): print("@", end = "");
            else: print("-", end = "");

def Copymap (): 
    global mxRow, mxCol, map_, newMap;
    for row in range(mxRow): 
        for col in range(mxCol): 
            map_[row][col] = newMap[row][col];

def access (): 
    global mxRow, mxCol, Dead, Alive, map_, newMap;
    ans = 'y';
    while (ans == 'y'): 
        for row in range(mxRow): 
            for col in range(mxCol): 
                cnt = Neighbors(row, col);
                if (cnt == 0 or cnt == 1 or cnt == 6 or cnt == 7 or cnt == 8): newMap[row][col] = Dead;
                elif (cnt == 2 or cnt == 3): newMap[row][col] = map_[row][col];
                elif (cnt == 4 or cnt == 5): newMap[row][col] = Alive;

        Copymap();
        while (True): 
            ans = input("\n\nContinue next Generation? (y/n)");
            if (ans == 'y' or ans == 'n'): break;
        if (ans == 'y'): output_map();
            

if __name__ == "__main__": 
    init();
    output_map();
    access();