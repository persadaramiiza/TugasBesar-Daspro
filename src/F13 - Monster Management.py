def print_table(data):
    # Get headers and rows
    headers = []
    for key in data:
        headers.append(key)
    rows = []
    for values in data.values():
        rows.append(values)

    # Find maximum lengths
    max_lengths = []
    for i in range(len(headers)):
        max_len = len(headers[i])
        j = 0
        while j < len(rows[i]):
            if len(str(rows[i][j])) > max_len:
                max_len = len(str(rows[i][j]))
            j += 1
        max_lengths.append(max_len)

    # Print headers
    i = 0
    while i < len(headers):
        print(f"{headers[i]:<{max_lengths[i]}} |", end='')
        i += 1
    print()

    # Find longest row length
    longest_row = 0
    i = 0
    while i < len(rows):
        if len(rows[i]) > longest_row:
            longest_row = len(rows[i])
        i += 1

    # Print rows
    i = 0
    while i < longest_row:
        j = 0
        while j < len(headers):
            if i < len(rows[j]):
                value = rows[j][i]
            else:
                value = "None"
            print(f"{value:<{max_lengths[j]}} |", end='')
            j += 1
        print()
        i += 1

ascii_monster = r'''
 ___  ________ _   _  _____ _____ ___________  ___  ___  ___   _   _   ___  _____  ________  ___ _____ _   _ _____ 
|  \/  |  _  | \ | |/  ___|_   _|  ___| ___ \ |  \/  | / _ \ | \ | | / _ \|  __ \|  ___|  \/  ||  ___| \ | |_   _|
| .  . | | | |  \| |\ `--.  | | | |__ | |_/ / | .  . |/ /_\ \|  \| |/ /_\ \ |  \/| |__ | .  . || |__ |  \| | | |  
| |\/| | | | | . ` | `--. \ | | |  __||    /  | |\/| ||  _  || . ` ||  _  | | __ |  __|| |\/| ||  __|| . ` | | |  
| |  | \ \_/ / |\  |/\__/ / | | | |___| |\ \  | |  | || | | || |\  || | | | |_\ \| |___| |  | || |___| |\  | | |  
\_|  |_/\___/\_| \_/\____/  \_/ \____/\_| \_| \_|  |_/\_| |_/\_| \_/\_| |_/\____/\____/\_|  |_/\____/\_| \_/ \_/  
'''


# MONSTER MANAGEMENT SYSTEM

def monster_management():
    print(ascii_monster)
    while True:
        print(">>> \033[1m Monster\033[0m")
        print("Selamat datang di database Monster, silahkan pilih menu yang diinginkan:")
        print("1. Tampilkan semua Monster")
        print("2. Tambahkan Monster baru")
        aksi = input(">>> \033[1m Pilih Aksi : \033[0m",)

        while aksi != "1" and aksi != "2" and aksi != "keluar":
            print("Aksi tidak valid! Silahkan pilih aksi yang valid.")
            aksi = input(">>> \033[1m Pilih Aksi : \033[0m",)
        
        if aksi == "1":
            print_table(monster)

        elif aksi == "keluar":
            break
        elif aksi == "2":
            new_id = len(monster['id']) + 1
        
        new_type = validate_alpha_input("Masukkan nama/type Monster: ")
        while new_type in monster["type"]:
            print("Nama/Type Monster sudah ada di database! Silahkan masukkan monster type yang berbeda.")
            new_type = validate_alpha_input("Enter new monster type: ")
        
        new_atk_power = validate_integer_input("Masukkan attack power: ")
        new_def_power = validate_integer_input_2(50, "Masukkan defend power (0-50): ")
        new_hp = validate_integer_input("Masukkan HP Monster: ")
        print(f"Nama/type Monster : {new_type}")
        print(f"Attack Power : {new_atk_power}")
        print(f"Defense Power : {new_def_power}")
        print(f"HP Monster : {new_hp}")
            
        confirmation = input(">>> Tambahkan Monster ke database? (Y/N) : ")
        if confirmation == "Y":   
                # Menambahkan monster ke dictionary
            new_monster = {
            'id': new_id,
            'type': new_type,
            'atk_power': new_atk_power,
            'def_power': new_def_power,
            'hp': new_hp
            }
                
            for key in new_monster:
                monster[key].append(new_monster[key])
                
                print("New monster added successfully!")
                print_table(monster)
        elif confirmation == "N":
                print("Monster tidak ditambahkan ke database.")
