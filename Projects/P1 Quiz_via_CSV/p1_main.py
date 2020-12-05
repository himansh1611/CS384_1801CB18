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