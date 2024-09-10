
def intch(message):
    try:
        x = int(input(message))
        if x is int(x):
            return int(x)
        
    except:
        print("Please enter an integer")
        intch(message)


def enter_data():
    import csv
    import os
    while True:
        try:

            input_name = input("Please enter name of student: ")
            if input_name == "end":
                print("Exitting...")
                break

            input_roll = intch("Please enter roll_no of student: ")
            if input_roll =="end":
                print("Exitting...")
                break

            input_marks = intch("Please enter marks of student: ")
            if input_marks == "end":
                print("Exitting...")
                break

            input_att = intch("Please enter student's attendance: ")
            if input_att == "end":
                print("Exitting...")
                break

            data = [[input_name, input_roll, input_marks, input_att]]

            file = os.path.join(os.getcwd(), "Stu_dat.csv")

            if os.path.exists(file):
                with open(file, 'a', newline='') as csvfile:
                    header= ["Name","Roll_no","Marks", "Attendance"]
                    writeM = csv.writer(csvfile)
                    writeM.writerows(data)
            else:
                with open(file, 'w', newline='') as csvfile:
                    header= ["Name","Roll_no","Marks", "Attendance"]
                    write = csv.writer(csvfile)
                    write.writerow(header)
                    write.writerows(data)

            print("Data saved successfully!")
        except Exception as e:
            print(f"Error: {e}")
        print("**************************************")


def fail_analy():
    import csv
    import os
    try:
        print("**************************************")
        fail_marks = intch("Failing marks: ")
        Tot_marks = intch("Maximum marks: ")
        y= os.path.join(os.getcwd(), "Stu_dat.csv")
        with open(y, 'r') as csvfil:
            readcsv = csv.reader(csvfil)  
            next(readcsv)
            print("Students failed: ")
            for row in readcsv:
                if int(row[2]) < fail_marks:
                    print(f"Name = {row[0]}, Marks = {row[2]}/{Tot_marks}")
        print("**************************************")
    except Exception as e:
        print(f"Error: {e}")


def topper():
    import csv
    import os
    try:
        print("**************************************")
        Tot_marks = intch("Maximum marks: ")
        data= os.path.join(os.getcwd(), "Stu_dat.csv")
        
        students = []
        with open(data, 'r') as csvfil:
            readcsv = csv.reader(csvfil)  
            next(readcsv)
            for row in readcsv:
                students.append(row)

        marks = [int(row[2]) for row in students ]
        max_marks = max(marks)
        topper = [row for row in students if int(row[2]) == max_marks]

        y = len(topper)
        for x in range (0, y):
            print(f"Topper {x+1} = {topper[x][0]} with marks {max_marks}/{Tot_marks}")
        print("**************************************")
    except Exception as e:
        print(f"Error: {e}")


def top_st():
    import os
    import csv
    try:
        data= os.path.join(os.getcwd(), "Stu_dat.csv")
        students = []

        with open(data, 'r') as csvfil:
            readcsv = csv.reader(csvfil)  
            next(readcsv)
            for row in readcsv:
                students.append(row)

        students.sort(key=lambda x: int(x[2]), reverse=True)


        z = len(students)
        try:
            if z >= 10:
                print("**************************************")
                print("Top 10 Students:")
                for student in students[:10]:
                    print(f"Name: {student[0]}, Marks: {student[2]}")
                print("**************************************")

            elif 10 > z >=5: 
                print("**************************************")
                print("Top 3 Students:- ")
                for student in students[:3]:
                    print(f"Name: {student[0]}, Marks: {student[2]}")
                print("**************************************")

            elif z < 5:
                print("**************************************")
                print("Top 2 Students:- ")
                for student in students[:10]:
                    print(f"Name: {student[0]}, Marks: {student[2]}")
                print("**************************************")

            
        except Exception as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def cut_off():
    import csv
    import os
    try:
        data= os.path.join(os.getcwd(), "Stu_dat.csv")
        print("**************************************")
        new_marks = intch("New cut-off marks: ")

        students = []
        with open(data, 'r') as csvfil:
            readcsv = csv.reader(csvfil)  
            next(readcsv)
            for row in readcsv:
                students.append(row)

        passed = [row for row in students if int(row[2]) >= new_marks]
        y = len(passed)
        for x in range (0, y):
            print(f"Student {x+1} = {passed[x][0]} with marks {passed[x][2]}")
        print("**************************************")
    except Exception as e:
        print(f"Error: {e}")


def average():
    import csv
    import os
    try:
        data= os.path.join(os.getcwd(), "Stu_dat.csv")
        
        students = []
        with open(data, 'r') as csvfil:
            readcsv = csv.reader(csvfil)  
            next(readcsv)
            for row in readcsv:
                students.append(row)

        marks = [int(row[2]) for row in students]
        total_marks = sum(marks)
        average_marks = total_marks / len(students)
        print(f"Average marks: {average_marks}")
        print("**************************************")
    except Exception as e:
        print(f"Error: {e}")

