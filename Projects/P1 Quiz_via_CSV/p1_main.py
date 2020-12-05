import os
import sys
import uuid
import time
import csv
import re
import threading
import sqlite3
import hashlib
from sqlite3 import Error
from pathlib import Path
import os.path

pwd = os.getcwd
root_folder = pwd()

db_path = os.path.join(root_folder, "project1_quiz_cs384.db")


def timelimit(input_file_path):
    headers = []
    with open(input_file_path, "r") as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            headers = row
            break
    x = len(headers)
    ya = headers[(x - 1)]
    time, yb = ya.split("=")
    pattern = re.compile(r"\d+")
    find_ = re.findall(pattern, yb)
    if find_:
        yc = int(find_[0])
        return yc


def cont_down(t):
    global quiz_usertimer

    quiz_usertimer = t * 60
    total_time_in_sec = quiz_usertimer

    for x in range(total_time_in_sec):
        quiz_usertimer = quiz_usertimer - 1
        time.sleep(1)


def create_hash_pass(password):
    q = uuid.uuid4().hex
    hashed_pass = hashlib.sha256(q.encode() + password.encode()).hexdigest()
    return hashed_pass + ":" + q


def check_password(hashed_password, user_password):
    hashpassword, q = hashed_password.split(":")
    hashed_pass = hashlib.sha256(q.encode() + user_password.encode()).hexdigest()
    if hashpassword == hashed_pass:
        return True
    else:
        return False


def open_reqdirectory(directory=".", pwd=pwd()):
    if directory == ".":
        return
    try:
        os.chdir(directory)
    except:
        os.mkdir(os.path.join(pwd, str(directory)))
        os.chdir(directory)
    return None


def append(file_name, headers, elements):
    if os.path.exists(file_name):
        with open(file_name, "a", newline="") as output_file:
            writer = csv.writer(output_file, delimiter=",")
            writer.writerow(elements)
    else:
        with open(file_name, "w", newline="") as output_file:
            writer = csv.writer(output_file, delimiter=",")
            writer.writerow(headers)
            writer.writerow(elements)


def open_reqcsv(input_file_path):
    data_list = []
    with open(input_file_path, "r") as input_file:
        reader = csv.DictReader(input_file)
        headers = reader.fieldnames
        for row in reader:
            data_list.append(row)
    return data_list


def create_db_file():
    try:
        with sqlite3.connect(db_path) as db:
            cursor = db.cursor()

        cursor.execute(
            """
		CREATE TABLE IF NOT EXISTS project1_registration
		(
			username	TEXT PRIMARY KEY NOT NULL ,
			password	TEXT NOT NULL ,
			name		CHAR(50) NOT NULL ,
			whatsapp_number		INT(10) NOT NULL
		)			"""
        )

        cursor.execute(
            """
		CREATE TABLE IF NOT EXISTS project1_marks
		(
			roll	VARCHAR(20) NOT NULL,
			quiz_num	INTEGER(1) NOT NULL,
			total_marks		INTEGER NOT NULL
		)			"""
        )
        db.commit()

    except Error as e:
        print(e)


def new_student_registration():
    create_db_file()
    q = 0
    while q == 0:
        username = input("Enter your rollNumber:	")
        while len(username) < 7:
            print("Please Try again")
            username = input("Enter your rollNumber:	")
        with sqlite3.connect(db_path) as db:
            cursor = db.cursor()
        find_user = "SELECT * FROM project1_registration WHERE username = ?"
        cursor.execute(find_user, [(username)])

        if cursor.fetchall():
            print("RollNumber already registered")
        else:
            q = 1

    name = input("Enter your Name(min_3 digits):	")
    while len(name) < 3:
        print("Please Try again")
        name = input("Enter your Name:	")

    whatsapp_number = input("Enter your Whatsapp_Number(10 digits):	")
    while len(whatsapp_number) != 10:
        print("Please Try again")
        whatsapp_number = input("Enter your Whatsapp_Number:	")

    password = input("Enter your password(min_8 digits):	")
    while len(password) < 8:
        print("Please Try again")
        password = input("Enter your password:	")

    password = create_hash_pass(password)
    password_1 = input("Please Enter your password again:	")
    while check_password(password, password_1) != True:
        print("Your password didn't match,Try again")
        password = input("Enter your password:	")
        password = create_hash_pass(password)
        password_1 = input("Please Enter your password again:	")

    with sqlite3.connect("project1_quiz_cs384.db") as db:
        cursor = db.cursor()
    insertData = """INSERT INTO project1_registration(username,password,name,whatsapp_number)
	VALUES(?,?,?,?)"""
    cursor.execute(insertData, [(username), (password), (name), (whatsapp_number)])
    db.commit()

    choice = input("Would you like to continue to take test?(y/n):	")
    if choice.lower() == "y":
        login_procedure()
    else:
        print("Goodbye!")
        time.sleep(1)

    return None


def quiz_res(filename, quiz_num, username):
    open_reqdirectory(root_folder)
    open_reqdirectory("individual" + "_" + "responses")
    raw_data = open_reqcsv(filename)
    correct_choice = 0
    wrong_choice = 0
    positive_marks = 0
    negative_marks = 0
    unanswered = 0
    total_marks = 0
    total_questions = 0
    total_answered = 0
    total_marks = 0
    for row in raw_data:
        if row["compulsory"] == "y":
            if row["marked_choice"] == row["correct_option"]:
                correct_choice += 1
                positive_marks += int(row["marks_correct_ans"])
            elif row["marked_choice"] != row["correct_option"]:
                wrong_choice += 1
                negative_marks += int(row["marks_wrong_ans"])
            else:
                unanswered += 1
                negative_marks += int(row["marks_wrong_ans"])
        else:
            if row["marked_choice"] == row["correct_option"]:
                correct_choice += 1
                positive_marks += int(row["marks_correct_ans"])
            elif row["marked_choice"] != row["correct_option"]:
                wrong_choice += 1
                negative_marks += int(row["marks_wrong_ans"])
            else:
                unanswered += 1
                negative_marks += 0
        total_questions += 1
        total_marks += int(row["marks_correct_ans"])

    total_usermarks = positive_marks + negative_marks
    total_answered = correct_choice + wrong_choice
    total = str(total_usermarks) + "/" + str(total_marks)

    print("Total Quiz Questions:	" + str(total_questions))
    print("Total Quiz Questions answered:	" + str(total_answered))
    print("Total Correct Question:	" + str(correct_choice))
    print("Total Wrong Questions:	" + str(wrong_choice))
    print("Total Marks: 	" + total)

    i = 0
    for row in raw_data:
        open_reqdirectory(root_folder)
        open_reqdirectory("individual" + "_" + "responses")
        file_name_1 = "q" + quiz_num + "_" + str(username) + ".csv"
        Headers_1 = [
            "ques_no",
            "question",
            "option1",
            "option2",
            "option3",
            "option4",
            "correct_option",
            "marks_correct_ans",
            "marks_wrong_ans",
            "compulsory",
            "marked_choice",
            "Total",
            "Legend",
        ]
        data_1 = []
        data_1.append(row["ques_no"])
        data_1.append(row["question"])
        data_1.append(row["option1"])
        data_1.append(row["option2"])
        data_1.append(row["option3"])
        data_1.append(row["option4"])
        data_1.append(row["correct_option"])
        data_1.append(row["marks_correct_ans"])
        data_1.append(row["marks_wrong_ans"])
        data_1.append(row["compulsory"])
        data_1.append(row["marked_choice"])

        if i == 0:
            data_1.append(str(correct_choice))
            data_1.append("CorrectChoices")
            i += 1
        elif i == 1:
            data_1.append(str(wrong_choice))
            data_1.append("Wrong Choices")
            i += 1
        elif i == 2:
            data_1.append(str(unanswered))
            data_1.append("Unanswered")
            i += 1
        elif i == 3:
            data_1.append(str(total_marks))
            data_1.append("Marks Obtained")
            i += 1
        elif i == 4:
            data_1.append(str(total_marks))
            data_1.append("Total Quiz Marks")
            i += 1
        else:
            data_1.append("		")
            data_1.append("		")

        append(file_name_1, Headers_1, data_1)

    open_reqdirectory(root_folder)
    open_reqdirectory("individual" + "_" + "responses")
    cwd = os.getcwd()
    file_path = Path(cwd + "/" + filename)
    file_path.unlink()

    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
    insertData = """INSERT INTO project1_marks(roll,quiz_num,total_marks)
	VALUES(?,?,?)"""
    cursor.execute(insertData, [(username), (quiz_num), (total)])
    db.commit()

    open_reqdirectory(root_folder)
    open_reqdirectory("quiz_wise_responses")
    file_name_2 = "scores_q" + quiz_num + ".csv"
    Headers_2 = [
        "Username",
        "Positive_marks_scored",
        "Negative_marks_scored",
        "Total_marks_scored",
        "Total_marks",
    ]
    data_2 = [username, positive_marks, negative_marks, total_marks, total_marks]
    append(file_name_2, Headers_2, data_2)

    print("Goodbye!")
    return None


def quizprocedure(quiz_num, username):
    try:
        open_reqdirectory(root_folder)
        open_reqdirectory("individual" + "_" + "responses")
        cwd = os.getcwd()
        file = "q" + quiz_num + "_" + str(username) + ".csv"
        file_path = Path(cwd + "/" + file)
        file_path.unlink()
    except:
        open_reqdirectory(root_folder)
        open_reqdirectory("quiz_wise_questions")
        raw_data = open_reqcsv("q" + quiz_num + ".csv")

        xy = timelimit("q" + quiz_num + ".csv")
        cont_down_thread = threading.Thread(target=cont_down, args=(xy,))
        cont_down_thread.start()

        for row in raw_data:
            if quiz_usertimer >= 0:
                print("		")
                my_time = quiz_usertimer
                a = int(my_time) // 60
                a = str(a)
                b = int(my_time) % 60
                b = str(b)
                print("Time_Left is " + a + ":" + b)
                print(row["ques_no"] + ")" + row["question"])
                print("Option 1)" + row["option1"])
                print("Option 2)" + row["option2"])
                print("Option 3)" + row["option3"])
                print("Option 4)" + row["option4"])
                print("		")
                print("Credits if Correct Option: " + row["marks_correct_ans"])
                print("Negative Marking: " + row["marks_wrong_ans"])
                print("Is compulsory: " + row["compulsory"])
                time.sleep(0.5)
                print("		")
                if row["compulsory"] == "n":
                    print("Enter Choice: 1, 2, 3, 4, S : S is to skip question")
                    chosen_answer = input("Your Choice:	")
                else:
                    print("Enter Choice: 1, 2, 3, 4")
                    chosen_answer = input("Your Choice:	")

                open_reqdirectory(root_folder)
                open_reqdirectory("individual" + "_" + "responses")
                file_name = "q" + quiz_num + "_0" + str(username) + ".csv"
                Headers = [
                    "ques_no",
                    "question",
                    "option1",
                    "option2",
                    "option3",
                    "option4",
                    "correct_option",
                    "marks_correct_ans",
                    "marks_wrong_ans",
                    "compulsory",
                    "marked_choice",
                ]
                data = []
                data.append(row["ques_no"])
                data.append(row["question"])
                data.append(row["option1"])
                data.append(row["option2"])
                data.append(row["option3"])
                data.append(row["option4"])
                data.append(row["correct_option"])
                data.append(row["marks_correct_ans"])
                data.append(row["marks_wrong_ans"])
                data.append(row["compulsory"])
                if row["compulsory"] == "n":
                    if chosen_answer == "1" or "2" or "3" or "4":
                        data.append(chosen_answer)
                    else:
                        data.append("	")
                        pass
                else:
                    data.append(chosen_answer)
                    pass
                open_reqdirectory(root_folder)
                open_reqdirectory("individual" + "_" + "responses")
                append(file_name, Headers, data)
                os.system("cls")

            else:
                chosen_answer = "	"
                open_reqdirectory(root_folder)
                open_reqdirectory("individual" + "_" + "responses")
                file_name = "q" + quiz_num + "_0" + str(username) + ".csv"
                Headers = [
                    "ques_no",
                    "question",
                    "option1",
                    "option2",
                    "option3",
                    "option4",
                    "correct_option",
                    "marks_correct_ans",
                    "marks_wrong_ans",
                    "compulsory",
                    "marked_choice",
                ]
                data = []
                data.append(row["ques_no"])
                data.append(row["question"])
                data.append(row["option1"])
                data.append(row["option2"])
                data.append(row["option3"])
                data.append(row["option4"])
                data.append(row["correct_option"])
                data.append(row["marks_correct_ans"])
                data.append(row["marks_wrong_ans"])
                data.append(row["compulsory"])
                data.append(chosen_answer)
                open_reqdirectory(root_folder)
                open_reqdirectory("individual" + "_" + "responses")
                append(file_name, Headers, data)

        quiz_res("q" + quiz_num + "_0" + str(username) + ".csv", quiz_num, username)

    return None

def login_procedure():
    i = 0
    while i < 5:
        user_name = input("Enter the username:	")
        pass_word = input("Enter the password:	")
        with sqlite3.connect(db_path) as db:
            cursor = db.cursor()
        cursor.execute("SELECT * FROM 'project1_registration' ")
        find_user = cursor.fetchall()
        for row in find_user:
            username = row[0]
            password = row[1]
            if check_password(password, pass_word):
                i = 8
                print(
                    """Enter the quiz_number you wish to take:
								1.q1
								2.q2
								3.q3							
					"""
                )
                quiz_num = str(input("Your Choice:	"))
                if quiz_num != "1" or "2" or "3":
                    print("Please try again")
                    quiz_num = str(input("your Choice:	"))
                quizprocedure(quiz_num, user_name)
                break
        else:
            print("username and password are not recognized")
            again = input("Do you want to try again? (y/n):	")
            if again.lower() == "n":
                print("Goodbye!")
                time.sleep(1)
                break
            elif again.lower() == "y":
                login_procedure()
            else:
                break
    return None


def main_menu():
    print("""Enter Your Choice: 1.Student Registration 2.Login to take quiz""")
    user_selection = int(input("Your Choice:	"))
    if user_selection == 1:
        new_student_registration()
    elif user_selection == 2:
        login_procedure()
    else:
        print("Picked invalid choice")
        main_menu()


main_menu()