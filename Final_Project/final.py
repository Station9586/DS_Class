from Course import *
from Student import *

# courses = Initial_Course();
subject_score = Initial_subject_score();
order = get_recommanded_order();

course_data = get_course_data();

Insert_Default_Data();

con = "y";
if __name__ == "__main__": 
    choice = 0;
    while (con == "y" or con == "Y"): 
        print("=" * 60);
        print("| \t1. Add student                                      |");
        print("| \t2. Add course to student                            |");
        print("| \t3. Add score to student                             |");
        print("| \t4. Show student course                              |");
        print("| \t5. Show student grade                               |");
        print("| \t6. Is pass student?                                 |");
        print("| \t7. Get recommended order of Choosing courses        |");
        print("| \t8. Get pass student of the course                   |");
        print("| \t9. Get k popular courses                            |");
        print("| \t10. Show prerequisite of course                     |");
        print("| \t11. Show Student who Choose this course             |");
        print("| \t12. Show all students and id                        |");
        print("| \t-1. Exit                                            |");
        print("=" * 60);
        print();
        print("Enter your choice: ", end = "");
        try: 
            choice = int(input());
        except ValueError:
            print("Please enter a number between 1 ~ 12 or -1.\n");
            continue;
        print();
        if (choice == 1): 
            print("Enter student name: ", end = "");
            name = input();
            print("Enter student id: ", end = "");
            try: id = int(input());
            except ValueError: 
                print("Please enter a number.\n");
                continue;
            add_student(id, name);
            print();
        elif (choice == 2): 
            print("Enter student name: ", end = "");
            name = input();
            print("Enter course name: ", end = "");
            course = input();
            add_course_by_name(name, course);
            print();
        elif (choice == 3): 
            print("Enter student name: ", end = "");
            name = input();
            print("Enter course name: ", end = "");
            course = input();
            print("Enter score: ", end = "");
            try: score = int(input());
            except ValueError: 
                print("Please enter a number between 0 ~ 100.\n");
                continue;
            if (score > 100 or score < 0): 
                print("Please enter a number between 0 ~ 100.");
                # continue;
            else: add_score_by_name(name, course, score);
            print();
        elif (choice == 4): 
            print("Enter student name: ", end = "");
            name = input();
            show_student_course_by_name(name);
            print();
        elif (choice == 5): 
            print("Enter student name: ", end = "");
            name = input();
            show_student_grade_by_name(name);
            print();
        elif (choice == 6): 
            print("Enter student name: ", end = "");
            name = input();
            ret = isPass(name);
            if (ret is None): 
                print(f"Student {name} does not exist.");
            else: 
                print(f"{name} pass:", end = "");
                if (len(ret) == 0): print(" None");
                else: 
                    for i in ret: print(f" {i}", end = ",\n"[i == ret[-1]]);
            print();
        elif (choice == 7): 
            print("Recommended order: ");
            for i in range(len(order)): 
                print(f"{i + 1}. {order[i]}");
            print();
        elif (choice == 8): 
            print("Enter course name: ", end = "");
            course = input();
            ret = get_pass_student(course);
            if (ret is not None and len(ret) != 0): 
                print(f"Student who pass {course}: ", end = "");
                for i in ret: print(i, end = ",\n"[i == ret[-1]]);
            print();
        elif (choice == 9): 
            print("Enter k: ", end = "");
            try: k = int(input());
            except ValueError: 
                print("Please enter a number.\n");
                continue;
            if (k <= 0): print("Please enter a number greater than 0.");
            ret = get_k_popular(k);
            if (ret is not None and len(ret) != 0): 
                a = 1;
                for i in ret: 
                    print(f"{a}. {i.name}, Number of people: {i.val}");
                    a += 1;
            print();
        elif (choice == 10): 
            print("Enter course name: ", end = "");
            course = input();
            if (course not in course_data): 
                print(f"Course {course} does not exist.\n");
                continue;
            print(f"Prerequisite of {course}: ", end = "");
            print(course_data[course].prerequisites);
            print();
        elif (choice == 11):
            print("Enter course name: ", end = "");
            course = input();
            show_student_who_choose_course(course);
            print();
        elif (choice == 12):
            print("All students: ", end = "\n");
            students_data = get_student_data();
            a = 1;
            for i in students_data: 
                print(f"{a}. {i.name} {i.id}");
                a += 1;
            print();
        elif (choice == -1): break;
        else: 
            print("Please enter a number between 1 ~ 12 or -1.");
            continue;
        print("continue? [y/n] ", end = "");
        con = input();
        print();
