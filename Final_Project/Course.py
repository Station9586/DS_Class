from que import Queue
import pandas as pd
from tree import *
from deap import MaxHeap


class Course:
    def __init__(self, name, grade, prerequisite = None) -> None:
        self.course = name;
        self.people = 0;
        self.mx = 30;
        self.students = Queue();
        self.recommended_grade = grade;
        self.prerequisites = prerequisite;
    
    def add_student(self, student):
        if (self.people < self.mx): 
            self.people += 1;
            self.students.push(student);
        else: 
            print(f"Course {self.course} is full.");


courses = pd.read_csv("course.csv");

Subjects = courses["Subject"].tolist();
Prerequisite = courses["Prerequisite"].tolist();
Recommended_grade = courses["Recommended_Grade"].tolist();

popularity = MaxHeap();


def Initial_Course (): 
    Course_dict = {};
    for i in range(len(Subjects)): 
        Course_dict[Subjects[i]] = Course(Subjects[i], Recommended_grade[i], Prerequisite[i]);
    return Course_dict;

def get_subjects (): return Subjects;

def get_prerequisites (): return Prerequisite;

def get_Recommended_Grade (): return Recommended_grade;

def Initial_subject_score (): 
    subject_score = {};
    for i in range(len(Subjects)): 
        subject_score[Subjects[i]] = None;
    return subject_score;

def insert_subject_score (course, k, name): 
    global subject_score;
    subject_score[course] = insert(subject_score[course], k, name);

def get_recommanded_order (): 
    gp = {};
    In = {};
    grade = [[] for _ in range(5)];
    for i in range(len(Subjects)): gp[Subjects[i]] = [];
    for i in range(len(Subjects)): 
        if (Prerequisite[i] != "None"): 
            gp[Prerequisite[i]].append(Subjects[i]);
            if (Subjects[i] in In): In[Subjects[i]] += 1;
            else: In[Subjects[i]] = 1;
        else: 
            # print(Recommended_grade[i]);
            grade[Recommended_grade[i]].append(Subjects[i]);

    q = Queue();
    for i in range(len(Subjects)): 
        if (Subjects[i] not in In): q.push(Subjects[i]);

    order = [];
    nw = 1;

    rec = dict(zip(Subjects, Recommended_grade));
    
    while (not q.empty()): 
        u = q.front();
        if (rec[u] > nw):
            nw = rec[u];
            for i in grade[nw]: order.append(i);
        if (u not in order): order.append(u);
        q.pop();
        for i in range(len(gp[u])): 
            v = gp[u][i];
            In[v] -= 1;
            if (In[v] == 0): q.push(v);
    
    return order;

def add_student_to_course (course_dict, student, course): 
    if (course in course_dict): 
        # course_dict[course].add_student(student);
        if (popularity.search(course)): 
            # print(f"{course} find");
            popularity.modify(course, course_dict[course].people);
        else: popularity.insert(course_dict[course].people, course);
    else: print(f"Course {course} does not exist.");


def get_k_popular (k): return popularity.get_first_k_value(k);

course_data = Initial_Course();
subject_score = Initial_subject_score();

def get_pass_student (course): 
    if (course in course_data): 
        subject_score[course], ret = passed_student(subject_score[course]);
        if (len(ret) == 0): print(f"No student passed {course} or No one choose this class.");
        return ret;
    else: 
        print(f"Course {course} does not exist.");
        return None;

def get_course_data (): return course_data;

def get_subject_score (): return subject_score;

def get_popularity (): return popularity;

def show_student_who_choose_course (course): 
    if (course in course_data): 
        print("Student who choose the course: ", end = "");
        course_data[course].students.Print();
    else: print(f"Course {course} does not exist.");
