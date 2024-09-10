import csv
import os
from processes import intch, enter_data, fail_analy, top_st, topper, cut_off, average

while True: 
    print("\n1. Import data from another CSV file")
    print("2. Enter data manually")
    print("3. Perform Analysis")
    print("4. Exit")
    
    choice = intch("Enter your choice: ")

    if choice == 1:
        filepath = input("Enter the path of the CSV file: ")

        try:
            with open(filepath, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                
                data= []
                for row in reader:
                    data.append(row)

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
            print("Data added succesfully.")

        except Exception as e:
            print(f"Error: {e}")

        print("**************************************")
        print("\n1) List by Cut-Off. \n2) Topper \n3) Students Failed. \n4) Top students list. \n5) Average marks. \n6) Exit.... ")
        choose = intch("Choose option: ")
        
        if choose ==1:
            cut_off()

        elif choose == 2:
            topper()

        elif choose == 3:
            fail_analy()

        elif choose == 4:
            top_st()

        elif choose == 5:
            average()

        elif choose == 6:
            break



    if choice == 2: 
        print("Enter the data manually:")
        data = enter_data()

        print("**************************************")
        print("\n1) List by Cut-Off. \n2) Topper \n3) Students Failed. \n4) Top students list. \n5) Average marks. \n6) Exit....")
        choose1 = intch("Choose option: ")
        
        if choose1 ==1:
            cut_off()

        elif choose1 == 2:
            topper()

        elif choose1 == 3:
            fail_analy()

        elif choose1 == 4:
            top_st()

        elif choose1 == 5:
            average()

        elif choose1 == 6:
            break

    if choice == 3:
        print("**************************************")
        print("\n1) List by Cut-Off. \n2) Topper \n3) Students Failed. \n4) Top students list. \n5) Average marks. \n6) Exit....")
        choose2 = intch("Choose option: ")
        
        if choose2 ==1:
            cut_off()

        elif choose2 == 2:
            topper()

        elif choose2 == 3:
            fail_analy()

        elif choose2 == 4:
            top_st()

        elif choose2 == 5:
            average()

        elif choose2 == 6:
            break
   

    
    if choice == 4:
        print("Exiting...")
        print("**************************************")
        break

