# 資料結構第二周作業
def Convert(S):  # 多項式轉換成list
    a = S.replace("x^", " ").replace("+", " ").replace("-", " -");
    s = list(map(int, a.split()));
    if (len(s) & 1): s.append(0);
    l = len(s) >> 1;
    for i in range(0, len(s), 2): s[i], s[i + 1] = s[i + 1], s[i];
    ret = [-1, l] + s;
    return ret;


def Padd(A, B):  # 多項式list相加
    mx = max(A[2], B[2]) + 1;
    cal = [0] * mx;
    a = A[2::];
    b = B[2::];
    for i in range(1, len(a), 2): cal[a[i - 1]] += a[i];
    for i in range(1, len(b), 2): cal[b[i - 1]] += b[i];
    ret = [];
    for i in range(len(cal) - 1, -1, -1): 
        if (cal[i] == 0): continue;
        ret.extend([i, cal[i]]);
    l = len(ret) >> 1;
    ret = [-1, l] + ret;
    return ret;


def Psub(A, B):  # 多項式list相減
    mx = max(A[2], B[2]) + 1;
    cal = [0] * mx;
    a = A[2::];
    b = B[2::];
    for i in range(1, len(a), 2): cal[a[i - 1]] += a[i];
    for i in range(1, len(b), 2): cal[b[i - 1]] -= b[i];
    ret = [];
    for i in range(len(cal) - 1, -1, -1): 
        if (cal[i] == 0): continue;
        ret.extend([i, cal[i]]);
    l = len(ret) >> 1;
    ret = [-1, l] + ret;
    return ret;


def Mul(A, B):  # 使用者呼叫多項式乘法
    ret = Mul_compute(A, B);
    return ret;


def Deconvert(A):  # 轉換回方程式
    s = A[2::];
    ret = "";
    for i in range(1, len(s), 2): 
        if (s[i] == 0): continue;
        if (s[i - 1] == 0): ret += f"{s[i]}";
        elif (s[i] > 0 and i != 1): ret += f"+{s[i]}x^{s[i - 1]}";
        else: ret += f"{s[i]}x^{s[i - 1]}";
    return ret;


def Mul_compute(A, B):  # 多項式乘法計算 A:多項式list B:多項式B的個別項次
    mx = A[2] + B[2] + 1;
    cal = [0] * mx;
    a = A[2::];
    b = B[2::];
    for i in range(1, len(a), 2): 
        for j in range(1, len(b), 2): 
            cal[a[i - 1] + b[j - 1]] += a[i] * b[j];
    ret = [];
    for i in range(len(cal) - 1, -1, -1): 
        if (cal[i] == 0): continue;
        ret.extend([i, cal[i]]);
    l = len(ret) >> 1;
    ret = [-1, l] + ret;
    return ret;

###------請勿更動此區塊-------------------------------------
def main():
    t1 = Convert("-2x^7+8x^5-9")
    t2 = Convert("1x^19+6x^7")
    print(f"t1: {t1}");
    print(f"t2: {t2}");
    print(Deconvert(Mul(t1, t2)))  # 多項式相乘
    print(Deconvert(Psub(t1, t2)))  # 多項式相減
    print(Deconvert(Padd(t1, t2)));
    
main()
###------請勿更動此區塊-------------------------------------