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
