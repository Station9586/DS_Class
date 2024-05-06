import sys


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.llink = None
        self.rlink = None


head = None;

def insert_f(name, score):
    global head;

    nw = Student(name, score);

    if (head is None): head = nw;
    else: 
        cur = head;
        while (cur.rlink): cur = cur.rlink;
        cur.rlink = nw;
        nw.llink = cur;

def swap (a, b):
    global head;

    if (a == b): return;
    if (a.llink): a.llink.rlink = b;
    else: head = b;
    if (b.rlink): b.rlink.llink = a;
    a.rlink, b.rlink = b.rlink, a;
    a.llink, b.llink = b, a.llink;

def display_f():
    global head

    count = 0

    if head == None:
        print('\n No student record!')
    else:
        print('\n%-15s %5s' % ("Name", "SCORE"))
        current = head;
        while current:
            print('%-15s %-3d' % (current.name, current.score))
            count += 1
            current = current.rlink
        print('Total %d record(s) found!' % count)


def adjust_right ():
    global head;
    if (head is None): return;
    end = None;
    while (end != head):
        cur = head;
        while (cur.rlink != end):
            if (cur.score < cur.rlink.score): swap(cur, cur.rlink);
            else: cur = cur.rlink;
        end = cur;

def main():
    global head
    option = 0

    while True:
        print()
        print('1.Insert')
        print('2.Display')
        print('3.Adjust')
        print('4.Exit')

        try:
            option = int(input("Choice:"))
        except ValueError:
            print()
            print('Not a correct number')
            print('Try again\n')
        if option == 1:
            insert_f("a", 1)
            insert_f("b", 7)
            insert_f("c", 9)
            insert_f("d", 3)
            insert_f("e", 6)
            insert_f("f", 5)
        elif option == 2:
            display_f()
        elif option == 3:
            adjust_right()
        elif option == 4:
            sys.exit(0)


main()