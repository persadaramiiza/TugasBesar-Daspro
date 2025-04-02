def valid_username(username: str) -> bool:
    valid_characters: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
    for char in username:
        if char not in valid_characters:
            return False
    return True

def exist_username(user: dict, username: str) -> bool:
    for id in user:
        if id != "atribut":
            if user['user id'][id] == username:
                return True
    return False

def register_account():
    global monster
    while True:
        username = input("Silahkan Masukkan Username: ")
        password = input("Silahkan Masukkan Password: ")

        if exist_username(user_info, username):
            print(f'Username {username} sudah terpakai, silahkan gunakan username lain!')
        else:
            monsters = monster['type']
            index = 1
            for monsta in monsters:
                print(f"{index}. {monsta}")
                index += 1

            choice = validate_integer_input_2(len(monsters), "Monster Pilihanmu: ")
            chosen_monster = monsters[choice - 1]

            print(f"Selamat datang Agent {username}. Bersama {chosen_monster}, ayo kita lawan musuh musuh itu!")
            return (str(len(user_info) + 1)), username, password, choice
        
        # Register a new user and append them to the existing user data