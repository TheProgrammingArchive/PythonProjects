import passwords
from passwords import class1, class2, class3, class4, class5
import os
import time
import random

def Class1():
    i = 0
    print("Please enter your password: ")
    password = input()
    while(password != class1):
        print("Invalid password!")
        password = input("Please try again: ")
    print("\n\n\n\n")
    print("1 --> Edit class")
    print("2 --> View class")
    print("3 --> Delete class")
    print("4 --> Return to main")
    option = int(input("Please enter an option to proceed: "))
    while (option > 4 or option < 1):
        print("Invalid option! Please enter a valid option: ")
        option = int(input())
    if (option == 1):
        entry = int(input("How many entries are you going to enter?: "))
        print(f"MAX ENTRY LIMIT = {entry}")
        file1 = open("class1.txt", "a")
        while(i < entry):
            Student_Name = input("Please enter the name of the student: ")
            Mother_Name = input("Please enter the name of the mother: ")
            Father_Name = input("Please enter the name of the father: ")
            Mob_num = input("Please enter the mobile number of the student: ")
            Roll_num = input("Please enter the roll number of the student: ")
            ProgAct_num = input("Progact number (Please enter a proper progact number): ")
            file1.write(f"{ProgAct_num}. \t {Student_Name} \t {Mother_Name} \t {Father_Name} \t {Mob_num} \t {Roll_num} \n\n")
            i = i + 1
        file1.close()
    elif(option == 2):
        print("\n\n\n\n")
        file1 = open("class1.txt", "r")
        for each in file1:
            print(each)
    elif(option == 3):
        print("\n\n")
        print("FILE DELETE")
        conf = input("Type DELETE to delete the file: ")
        if(conf == "DELETE"):
            os.remove("class1.txt")
            print("File deleted")
        else:
            print("File not deleted")
    elif(option == 4):
        print("Returning to main\n\n")

def Class2():
    i = 0
    print("Please enter your password: ")
    password = input()
    while(password != class2):
        print("Invalid password!")
        password = input("Please try again: ")
    print("\n\n\n\n")
    print("1 --> Edit class")
    print("2 --> View class")
    print("3 --> Delete class")
    print("4 --> Return to main")
    option = int(input("Please enter an option to proceed: "))
    while (option > 4 or option < 1):
        print("Invalid option! Please enter a valid option: ")
        option = int(input())
    if (option == 1):
        entry = int(input("How many entries are you going to enter?: "))
        print(f"MAX ENTRY LIMIT = {entry}")
        file2 = open("class2.txt", "a")
        while(i < entry):
            Student_Name = input("Please enter the name of the student: ")
            Mother_Name = input("Please enter the name of the mother: ")
            Father_Name = input("Please enter the name of the father: ")
            Mob_num = input("Please enter the mobile number of the student: ")
            Roll_num = input("Please enter the roll number of the student: ")
            ProgAct_num = input("Progact number (Please enter a proper progact number): ")
            file2.write(f"{ProgAct_num}. \t {Student_Name} \t {Mother_Name} \t {Father_Name} \t {Mob_num} \t {Roll_num} \n\n")
            i = i + 1
        file2.close()
    elif(option == 2):
        print("\n\n\n\n")
        file2 = open("class2.txt", "r")
        for each in file2:
            print(each)
    elif(option == 3):
        print("\n\n")
        print("FILE DELETE")
        conf = input("Type DELETE to delete the file: ")
        if(conf == "DELETE"):
            os.remove("class2.txt")
            print("File deleted")
        else:
            print("File not deleted")
    elif(option == 4):
        print("Returning to main\n\n")


def Class3():
    i = 0
    print("Please enter your password: ")
    password = input()
    while(password != class3):
        print("Invalid password!")
        password = input("Please try again: ")
    print("\n\n\n\n")
    print("1 --> Edit class")
    print("2 --> View class")
    print("3 --> Delete class")
    print("4 --> Return to main")
    option = int(input("Please enter an option to proceed: "))
    while (option > 4 or option < 1):
        print("Invalid option! Please enter a valid option: ")
        option = int(input())
    if (option == 1):
        entry = int(input("How many entries are you going to enter?: "))
        print(f"MAX ENTRY LIMIT = {entry}")
        file3 = open("class3.txt", "a")
        while(i < entry):
            Student_Name = input("Please enter the name of the student: ")
            Mother_Name = input("Please enter the name of the mother: ")
            Father_Name = input("Please enter the name of the father: ")
            Mob_num = input("Please enter the mobile number of the student: ")
            Roll_num = input("Please enter the roll number of the student: ")
            ProgAct_num = input("Progact number (Please enter a proper progact number): ")
            file3.write(f"{ProgAct_num}. \t {Student_Name} \t {Mother_Name} \t {Father_Name} \t {Mob_num} \t {Roll_num} \n\n")
            i = i + 1
        file3.close()
    elif(option == 2):
        print("\n\n\n\n")
        file3 = open("class3.txt", "r")
        for each in file3:
            print(each)
    elif(option == 3):
        print("\n\n")
        print("FILE DELETE")
        conf = input("Type DELETE to delete the file: ")
        if(conf == "DELETE"):
            os.remove("class3.txt")
            print("File deleted")
        else:
            print("File not deleted")
    elif(option == 4):
        print("Returning to main\n\n")


def Class4():
    i = 0
    print("Please enter your password: ")
    password = input()
    while(password != class4):
        print("Invalid password!")
        password = input("Please try again: ")
    print("\n\n\n\n")
    print("1 --> Edit class")
    print("2 --> View class")
    print("3 --> Delete class")
    print("4 --> Return to main")
    option = int(input("Please enter an option to proceed: "))
    while (option > 4 or option < 1):
        print("Invalid option! Please enter a valid option: ")
        option = int(input())
    if (option == 1):
        entry = int(input("How many entries are you going to enter?: "))
        print(f"MAX ENTRY LIMIT = {entry}")
        file4 = open("class4.txt", "a")
        while(i < entry):
            Student_Name = input("Please enter the name of the student: ")
            Mother_Name = input("Please enter the name of the mother: ")
            Father_Name = input("Please enter the name of the father: ")
            Mob_num = input("Please enter the mobile number of the student: ")
            Roll_num = input("Please enter the roll number of the student: ")
            ProgAct_num = input("Progact number (Please enter a proper progact number): ")
            file4.write(f"{ProgAct_num}. \t {Student_Name} \t {Mother_Name} \t {Father_Name} \t {Mob_num} \t {Roll_num} \n\n")
            i = i + 1
        file4.close()
    elif(option == 2):
        print("\n\n\n\n")
        file4 = open("class4.txt", "r")
        for each in file4:
            print(each)
    elif(option == 3):
        print("\n\n")
        print("FILE DELETE")
        conf = input("Type DELETE to delete the file: ")
        if(conf == "DELETE"):
            os.remove("class4.txt")
            print("File deleted")
        else:
            print("File not deleted")
    elif(option == 4):
        print("Returning to main\n\n")


def Class5():
    i = 0
    print("Please enter your password: ")
    password = input()
    while(password != class5):
        print("Invalid password!")
        password = input("Please try again: ")
    print("\n\n\n\n")
    print("1 --> Edit class")
    print("2 --> View class")
    print("3 --> Delete class")
    print("4 --> Return to main")
    option = int(input("Please enter an option to proceed: "))
    while (option > 4 or option < 1):
        print("Invalid option! Please enter a valid option: ")
        option = int(input())
    if (option == 1):
        entry = int(input("How many entries are you going to enter?: "))
        print(f"MAX ENTRY LIMIT = {entry}")
        file5 = open("class5.txt", "a")
        while(i < entry):
            Student_Name = input("Please enter the name of the student: ")
            Mother_Name = input("Please enter the name of the mother: ")
            Father_Name = input("Please enter the name of the father: ")
            Mob_num = input("Please enter the mobile number of the student: ")
            Roll_num = input("Please enter the roll number of the student: ")
            ProgAct_num = input("Progact number (Please enter a proper progact number): ")
            file5.write(f"{ProgAct_num}. \t {Student_Name} \t {Mother_Name} \t {Father_Name} \t {Mob_num} \t {Roll_num} \n\n")
            i = i + 1
        file5.close()
    elif(option == 2):
        print("\n\n\n\n")
        file5 = open("class5.txt", "r")
        for each in file5:
            print(each)
    elif(option == 3):
        print("\n\n")
        print("FILE DELETE")
        conf = input("Type DELETE to delete the file: ")
        if(conf == "DELETE"):
            os.remove("class5.txt")
            print("File deleted")
        else:
            print("File not deleted")
    elif(option == 4):
        print("Returning to main\n\n")

def menu():
    print("\t\t\t\tMENU\n\n")
    print("1 --> Teacher")
    print("2 --> Administrator")
    print("3 --> Exit")


def teacher():
    print("\t\t\t\tTeacher entry\t\t\t\t\n\n\n\n")
    print("1 --> Class 1")
    print("2 --> Class 2")
    print("3 --> Class 3")
    print("4 --> Class 4")
    print("5 --> Class 5")
    print("6 --> Exit teacher")
    Class_opt = int(input("Please enter your class: "))
    while(Class_opt > 6 or Class_opt < 1):
        Class_opt = int(input("Class value invalid! Please enter a valid class: "))
    if(Class_opt == 1):
        Class1()
    elif(Class_opt == 2):
        Class2()
    elif(Class_opt == 3):
        Class3()
    elif(Class_opt == 4):
        Class4()
    elif(Class_opt == 5):
        Class5()
    else:
        main()


#NPC SCHOOL MANAGEMENT SYSTEM
def main():
    print("\t\t\t\t\t\t\t\t\t\t\t\t\tNPC SCHOOL MANAGEMENT SYSTEM\t\t\t\t\t\t\t\n\n\n\n")
    menu()
    choice = int(input("Please enter your choice: "))
    while(choice > 3 or choice < 1):
        choice = input("Invalid option! Please try again: ")
    while(choice != 3):
        if(choice == 1):
            teacher()
        elif(choice == 2):
            print("Under development")
            main()
        elif(choice == 3):
            exit()
        else:
            print("Error code: 0x44")

main()