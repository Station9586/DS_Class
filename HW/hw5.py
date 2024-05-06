class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sumTwoReversedLinkedList(l1, l2):
    # Enter your code here
    up = 0;
    head = None;
    tail = None;

    while (l1 and l2):
        cal = l1.val + l2.val + up;
        nw = ListNode(cal % 10);
        up = cal // 10;
        if (head == None):
            head = nw;
            tail = nw;
        else:
            tail.next = nw;
            tail = tail.next;
        l1 = l1.next;
        l2 = l2.next;

    while (l1):
        cal = l1.val + up;
        nw = ListNode(cal % 10);
        up = cal // 10;
        if (head == None):
            head = nw;
            tail = nw;
        else:
            tail.next = nw;
            tail = tail.next;
        l1 = l1.next;

    while (l2):
        cal = l2.val + up;
        nw = ListNode(cal % 10);
        up = cal // 10;
        if (head == None):
            head = nw;
            tail = nw;
        else:
            tail.next = nw;
            tail = tail.next;
        l2 = l2.next;

    if (up != 0):
        nw = ListNode(up);
        if (head == None):
            head = nw;
            tail = nw;
        else:
            tail.next = nw;
            tail = tail.next;

    return head;


def main():
    l1 = ListNode(5, ListNode(8, ListNode(7, ListNode(9))))
    l2 = ListNode(2, ListNode(3, ListNode(4, ListNode(9, ListNode(9, ListNode(9))))))

    # l1 = ListNode(5, ListNode(6, ListNode(7, ListNode(8))))
    # l2 = ListNode(2, ListNode(3, ListNode(4)))
    output = sumTwoReversedLinkedList(l1, l2)
    while (output):
        print(output.val)
        output = output.next


main()