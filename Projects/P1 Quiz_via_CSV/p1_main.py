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