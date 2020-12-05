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