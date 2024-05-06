from AVL_tree import *
from doubly_Lnk import *
from que import *
from Course import *
from tree import *

course_data = get_course_data();
subject_score = get_subject_score();
popularity = get_popularity();

class Student: 
    def  __init__(self, id, name) -> None:
        self.id = id;
        self.name = name;
        self.course = DoublyLinkedList(); # what student choose
        self.grades = AVLTree(); # grades of student

    def add_course(self, course): 
        if (self.course.Search(course)): 
            print(f"Student {self.name} already choose {course}.");
            return False;
        if (course_data[course].people >= course_data[course].mx): 
            print(f"Course {course} is full.");
            return False;
        if (course_data[course].prerequisites == "None"): 
            self.course.push_back(course);
            return True;
        if (not self.course.Search(course_data[course].prerequisites)): 
            print(f"Student {self.name} does not have the prerequisites of {course}.");
            return False;
        self.course.push_back(course);
        return True;

    # def delete_course(self, course):
    #     if (self.course.Search(course)): self.course.delete(course);
    #     else: print(f"Student {self.name} does not choose {course}.");

    def add_grade(self, course, grade):
        self.grades.root = self.grades.insert_node(self.grades.root, course, grade);


students_data = [];
idx = {};
Len = 0;

all_name = [];
all_id = [];

def add_student (id, name): 
    global students_data, Len;
    if (id in all_id or name in all_name): 
        print(f"Student is already exists.");
        return;
    all_id.append(id);
    all_name.append(name);
    students_data.append(Student(id, name));
    idx[name] = Len;
    idx[id] = Len;
    Len += 1;

def add_course_by_name (name, course): 
    global students_data, idx;
    if (course not in course_data): 
        print(f"Course {course} does not exist.");
        return;
    if (name in idx): 
        if (students_data[idx[name]].add_course(course)):
            course_data[course].add_student(name);
            add_student_to_course(course_data, name, course);
    else: print(f"Student {name} does not exist.");

def add_course_by_id (id, course): 
    global students_data, idx;
    if (course not in course_data): 
        print(f"Course {course} does not exist.");
        return;
    if (id in idx): 
        if (students_data[idx[id]].add_course(course)):
            course_data[course].add_student(students_data[idx[id]].name);
            add_student_to_course(course_data, students_data[idx[id]].name, course);
    else: print(f"Student {id} does not exist.");

def add_score_by_name (name, course, score): 
    global students_data, idx;
    if (course not in course_data): 
        print(f"Course {course} does not exist.");
        return;
    if (name in idx): 
        if (not students_data[idx[name]].course.Search(course)): 
            print(f"Student {name} does not choose {course}.");
            return;
        if (students_data[idx[name]].grades.search_course(students_data[idx[name]].grades.root, course)): 
            print(f"Student {name} already has score of {course}.");
            return;
        students_data[idx[name]].add_grade(course, score);
        insert_subject_score(course, score, name);
    else: print(f"Student {name} does not exist.");

def add_score_by_id (id, course, score): 
    global students_data, idx;
    if (course not in course_data): 
        print(f"Course {course} does not exist.");
        return;
    if (id in idx): 
        if (not students_data[idx[id]].course.Search(course)): 
            print(f"Student {id} does not choose {course}.");
            return;
        if (students_data[idx[id]].grades.search_course(students_data[idx[id]].grades.root, course)): 
            print(f"Student {id} already has score of {course}.");
            return;    
        students_data[idx[id]].add_grade(course, score);
        insert_subject_score(course, score, students_data[idx[id]].name);
    else: print(f"Student {id} does not exist.");

def show_student_course_by_name (name): 
    global students_data, idx;
    if (name in idx): 
        print(f"Student {name} choose: ", end = "");
        students_data[idx[name]].course.Print();
    else: print(f"Student {name} does not exist.");

def show_student_course_by_id (id):
    global students_data, idx;
    if (id in idx): 
        print(f"Student {id} choose: ", end = "");
        students_data[idx[id]].course.Print();
    else: print(f"Student {id} does not exist.");

def show_student_grade_by_name (name):
    global students_data, idx;
    if (name in idx): 
        print(f"Student {name} grades: ", end = "\n");
        students_data[idx[name]].grades.inorder(students_data[idx[name]].grades.root);
        print();
    else: print(f"Student {name} does not exist.");

def show_student_grade_by_id (id):
    global students_data, idx;
    if (id in idx): 
        print(f"Student {id} grades: ", end = "\n");
        students_data[idx[id]].grades.inorder(students_data[idx[id]].grades.root);
        print();
    else: print(f"Student {id} does not exist.");

def isPass (name): 
    global students_data, idx;
    ret = [];
    def inorder (p):
        if (p != None): 
            inorder(p.left);
            if (p.score >= 60): ret.append(p.course);
            inorder(p.right);
    
    if (name in idx): 
        tmp = students_data[idx[name]].grades.root;
        inorder(tmp);
        return ret;
    return None;

def get_student_data (): return students_data;

def Insert_Default_Data (): 
    add_student(4111029007, "apple");
    add_student(4111029003, "banana");
    add_student(4111029012, "cat");
    add_student(4111029013, "dog");
    add_student(4111029014, "egg");
    add_student(4111029028, "fish");
    add_student(4111029030, "grape");

    # print(Subjects);

    add_course_by_name("apple", "Calculus");
    add_course_by_name("apple", "Linear Algebra");
    add_course_by_name("banana", "Financial Accounting");
    add_course_by_name("banana", "Economic");
    add_course_by_name("cat", "Financial Accounting");
    add_course_by_name("cat", "Programming");
    add_course_by_name("dog", "Programming");
    add_course_by_name("dog", "Essential of MIS");
    add_course_by_id(4111029014, "Management");
    add_course_by_id(4111029014, "Essential of MIS");
    add_course_by_id(4111029028, "Calculus");
    add_course_by_id(4111029028, "Linear Algebra");
    add_course_by_id(4111029030, "Computer Science");
    add_course_by_id(4111029030, "Programming");

    # add_course_by_name("apple", "Algorithm");

    # show_student_course_by_name("apple");
    # show_student_course_by_name("banana");
    # show_student_course_by_id(4111029012);
    # show_student_course_by_id(4111029013);
    # show_student_course_by_id(4111029014);
    # show_student_course_by_id(4111029028);
    # show_student_course_by_id(4111029030);

    # print();

    add_score_by_name("apple", "Calculus", 100);
    add_score_by_name("apple", "Linear Algebra", 100);
    add_score_by_name("banana", "Financial Accounting", 60);
    add_score_by_name("banana", "Economic", 60);
    add_score_by_name("cat", "Financial Accounting", 40);
    add_score_by_name("cat", "Programming", 40);
    add_score_by_name("dog", "Programming", 80);
    add_score_by_name("dog", "Essential of MIS", 80);
    add_score_by_id(4111029014, "Management", 60);
    add_score_by_id(4111029014, "Essential of MIS", 60);
    add_score_by_id(4111029028, "Calculus", 80);
    add_score_by_id(4111029028, "Linear Algebra", 30);
    add_score_by_id(4111029030, "Computer Science", 100);
    add_score_by_id(4111029030, "Programming", 70);

    # show_student_who_choose_course("Calculus");
    # show_student_grade_by_name("apple");
    # show_student_grade_by_name("banana");
    # show_student_grade_by_id(4111029012);
    # show_student_grade_by_id(4111029013);
    # show_student_grade_by_id(4111029014);
    # show_student_grade_by_id(4111029028);
    # show_student_grade_by_id(4111029030);
    # print();

    # ret = isPass("apple");
    # print(ret);
    # ret = isPass("banana");
    # print(ret);
    # ret = isPass(4111029012);
    # print(ret);
    # ret = isPass(4111029013);
    # print(ret);
    # ret = isPass(4111029014);
    # print(ret);
    # ret = isPass(4111029028);
    # print(ret);
    # ret = isPass(4111029030);
    # print(ret);
    # print();

    # print("Recommended order: ");
    # for i in range(len(order)): print(f"{i + 1}. {order[i]}");
    # print();

    # ret = get_pass_student("Calculus");
    # print(ret);
    # print();
    # ret = get_pass_student("Linear Algebra");
    # print(ret);
    # print();
    # ret = get_pass_student("Programming");
    # print(ret);
    # print();

    # popularity = get_popularity();
    # for i in popularity.heap: print(i.name, i.val);
    # print();

    # ret = get_k_popular(3);
    # for i in ret: print(i.name, i.val);
    # # print(ret);
    # print();