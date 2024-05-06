# Huffuman tree
class Node:
    def __init__(self, data, freq):
        self.data = data  # node的字母
        self.freq = freq  # node的頻率
        self.lch = None  # node的左子樹
        self.rch = None  # node的右子樹


class Huffman:
    def __init__(self, data, freq):
        self.data = data  # 霍夫曼樹的所有字母
        self.freq = freq  # 霍夫曼樹的所有頻率
        self.root = None  # 霍夫曼樹的根節點
        self.codes = {}  # 霍夫曼編碼的字典

    def build_tree(self):  # 建立霍夫曼樹
        mp = [Node(a, b) for a, b in zip(self.data, self.freq)]; # 先合併data & frequency的array
        while (len(mp) > 1): # 當mp長度 >= 2的時候就繼續合併 # 傻逼bubble sort
            self.node_sort(mp); # 每次都把 mp 由 小到大 排序
            for i in mp: print(i.data, i.freq);
            print()
            lch = mp.pop(0); # 左 節點是取 mp 中 最小 的, 並從mp中移除
            rch = mp.pop(0); # 右 節點取 mp 中 第二小 的, 並從mp中移除
            nw = Node(None, lch.freq + rch.freq); # 將lch & rch的frequency合併後建立一個新的節點
            nw.lch, nw.rch = lch, rch; # 新節點的lch & rch -> mp中前兩小的人
            mp.append(nw); # 將新節點放到mp裡面
            
        self.root = mp[0]; # mp合併完只會剩下一個人 => 根節點

    def solve (self, hm: Node, ret: str) -> None: 
        if (hm.data != None): self.codes[hm.data] = ret; # 當data不是None -> 已經找到字母了 -> 將ret賦予給data
        if (hm.lch != None): self.solve(hm.lch, ret + '0'); # lch還有人 -> 繼續找 -> ret + "0"
        if (hm.rch != None): self.solve(hm.rch, ret + '1'); # rch還有人 -> 繼續找 -> ret + "1"

    def get_codes(self):  # 將字母編碼，並回傳霍夫曼編碼結果
        self.solve(self.root, ""); # 呼叫solve, 從 root 開始遞迴下去找
        return self.codes;


############ 請勿修改以下程式碼############
    def node_sort(self, nodes):  # 將節點依照頻率排序
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                if nodes[i].freq > nodes[j].freq:
                    nodes[i], nodes[j] = nodes[j], nodes[i]
############ 請勿修改以下程式碼############


############ 請勿修改以下程式碼############
def main():
    data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # 字母列表(請注意，測試時會使用其他字母做測試)
    freq = [0.01, 0.24, 0.08, 0.2, 0.22, 0.12, 0.07, 0.06]  # 頻率列表(請注意，測試時會使用其他頻率做測試)
    # data = ['t', 'o', ' ', 'b', 'e', 'r', 'n'];
    # freq = [3, 4, 5, 2, 2, 1, 1];
    # data = ['f', 'o', 'r', 'g', 'e', 't']
    # freq = [2, 3, 4, 4, 5, 7]
    huffuman = Huffman(data, freq)  # 建立霍夫曼物件
    huffuman.build_tree()  # 建立霍夫曼樹
    encoded = huffuman.get_codes()  # 取得霍夫曼編碼
    print(encoded)  # 印出霍夫曼編碼

    # b = Huffman(data, freq);
    # b.build();
    # encode = b.get_codes();
    # print(encode);

main()
############ 請勿修改以下程式碼############
