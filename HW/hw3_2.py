mxN = 15;
square = [[0] * mxN for _ in range(mxN)];
n = 0;

def anykey_f (): 
    try:
        tChar = input("\n\n Press any key to continue...");
    except ValueError: 
        pass;

def init (): 
    global n;
    while (True): 
        n = int(input("\nEnter odd matrix size: "));
        if (not n & 1 or n <= 0 or n > 15): print("Should be > 0 and < 15 odd number", end = "");
        # else: break;
        break;

def Magic (): 
    global n, square;
    square[0][n >> 1] = 1;
    key = 2;
    i = 0;
    j = n >> 1;

    while (key <= n * n): 
        p = (i - 1) % n;
        q = (j + 1) % n;
        if (p < 0): q = n - 1;
        if (square[p][q]): i = (i + 1) % n;
        else:
            i = p;
            j = q;
        square[i][j] = key;
        key += 1;

def output (): 
    print(f"\n The {n} * {n} Magic Matrix");
    print("-" * 20);
    for i in range(n): 
        for j in range(n): 
            print("%-4d" % square[i][j], end = '');
        print();
    anykey_f();

if __name__ == "__main__": 
    init();
    Magic();
    output();