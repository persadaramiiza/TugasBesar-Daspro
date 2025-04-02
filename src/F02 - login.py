# F02 - Login
def exist_username(user: dict, username: str) -> bool:
    for i in range(len(user['id'])):
        if user['id'][i] != "Atribut":
            if user['username'][i] == username:
                return True
    return False

def wrong_password(user: dict, username: str, password: str):
    for i in range(len(user['id'])):
        if user['id'][i] != "Atribut":
            if user['username'][i] == username:
                IDUser = i
                break
    if str(user['password'][IDUser]) == password:
        return False
    return True

def login(user: dict) -> int:
    
    username = input("Username: ")
    password = input("Password: ")

    # cek username
    if not exist_username(user,username):
        print ("Username tidak terdaftar!")
        return -1

    # cek password
    elif wrong_password(user,username,password):
        print ("Password salah!")
        return -1

    else:
        IDUser: int = 0
        for i in range(len(user['id'])):
            if user['id'][i] != "Atribut":
                if user['username'][i] == username:
                    IDUser = i
                    break
        if user['role'][IDUser] == "agent":
            print(f"Selamat datang, Agent {username}!")
        else:
            print(f'Selamat datang, yang mulia admin {username}!')
        return IDUser