# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:52:40 2020

@author: kevin
"""

import sys


class Student:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.next = None


ptr = None
current = None
prev = None
head = Student()
head.next = head


def insert_f():  # 請完成老師上課的Circular Linked List程式碼
    global head, ptr, current, prev;
    ptr = Student();
    print("\n\n************ Insert Node ************\n");
    ptr.name = input("Please enter student name: ");
    ptr.score = eval(input("Please enter student score: "));
    print("\n***************************************\n");
    prev = head;
    current = head.next;
    while (current != head and current.score >= ptr.score): 
        prev = current;
        current = current.next;
    ptr.next = current;
    prev.next = ptr;


def delete_f():  # 請完成老師上課的Circular Linked List程式碼
    global head, current, prev;
    del_name = "";
    if (head.next == head): print("\n     No student record!!");
    else: 
        print("\n\n************ Delete Node ************\n");
        del_name = input("Please enter student name: ");
        prev = head;
        current = head.next;
        while (current != head and del_name != current.name): 
            prev = current;
            current = current.next;
        if (current != head): 
            prev.next = current.next;
            current = None;
            print(f"Student {del_name} record deleted");
        else: print(f"Student {del_name} not found");
    print("\n***************************************\n")



def dispaly_f():  # 請完成老師上課的Circular Linked List程式碼
    global head, current;
    cnt = 0;
    if (head.next == head): print("\n     No student record!!");
    else: 
        print("\n\n************ Display Node ************");
        print("%-15s %5s" % ("Name", "SCORE"));
        print("------------------------------------------");
        current = head.next;
        while (current != head):
            print("%-15s %-3d" % (current.name, current.score));
            cnt += 1;
            current = current.next;
        print("------------------------------------------");
        print(f" Total {cnt} record");
    print("\n***************************************\n");



def modify_f():  # 請完成老師上課的Circular Linked List程式碼
    global head, current, prev;
    if (head.next == head): print("\n     No student record!!");
    else: 
        print("\n\n************ Modify Node ************");
        modify_name = input(" Please enter student name: ");
        prev = head;
        current = head.next;
        while (current != head and modify_name != current.name): 
            prev = current;
            current = current.next;
        if (current != head): 
            print(f"\n   Student name: {current.name}");
            print(f"    Student score: {current.score}");
            prev.next = current.next;
            current = None;
            newScore = eval(input(" Please enter new score: "));
            ptr = Student();
            ptr.next = None;
            ptr.name = modify_name;
            ptr.score = newScore;
            prev = head;
            current = head.next;
            while (current != head and current.score >= ptr.score): 
                prev = current;
                current = current.next;
            ptr.next = current;
            prev.next = ptr;
        else: print(f"\n Student {modify_name} not found!\n");


def getsum_f():
    global head
    sum_score = get_sum(head)
    print()
    print('Sum score : %d \n' % sum_score)


def get_sum(current):
    """"""
    global head;
    if (current.next == head): return current.score;
    return current.score + get_sum(current.next);


def main():
    global head
    option = 0
    while True:
        print('1.Insert')
        print('2.Delete')
        print('3.Modify')
        print('4.Display')
        print('5.GetSum')
        print('6.Exit')
        try:
            option = int(input('pls select an option : '))
            if option == 1:
                insert_f()
            elif option == 2:
                delete_f()
            elif option == 3:
                modify_f()
            elif option == 4:
                dispaly_f()
            elif option == 5:
                getsum_f()
            elif option == 6:
                sys.exit(0)
            else:
                raise ValueError
        except ValueError:
            print('Not a correct number')
            print('Try again\n')


main()
