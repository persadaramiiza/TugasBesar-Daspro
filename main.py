import os
import time
from typing import Iterator, List
import argparse
import sys 




ascii_art_shop =r'''

███████╗██╗  ██╗ ██████╗ ██████╗ 
██╔════╝██║  ██║██╔═══██╗██╔══██╗
███████╗███████║██║   ██║██████╔╝
╚════██║██╔══██║██║   ██║██╔═══╝ 
███████║██║  ██║╚██████╔╝██║     
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
'''


ascii_art_battle = r'''

▄▄▄▄·  ▄▄▄· ▄▄▄▄▄▄▄▄▄▄▄▄▌  ▄▄▄ .    ▄▄ 
▐█ ▀█▪▐█ ▀█ •██  •██  ██•  ▀▄.▀·    ██▌
▐█▀▀█▄▄█▀▀█  ▐█.▪ ▐█.▪██▪  ▐▀▀▪▄    ▐█·
██▄▪▐█▐█ ▪▐▌ ▐█▌· ▐█▌·▐█▌▐▌▐█▄▄▌    .▀ 
·▀▀▀▀  ▀  ▀  ▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀      ▀ 

'''


ascii_art_arena = r'''
 █████╗ ██████╗ ███████╗███╗   ██╗ █████╗ 
██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔══██╗
███████║██████╔╝█████╗  ██╔██╗ ██║███████║
██╔══██║██╔══██╗██╔══╝  ██║╚██╗██║██╔══██║
██║  ██║██║  ██║███████╗██║ ╚████║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝
'''

ascii_art_laboratory = r'''

██╗      █████╗ ██████╗  ██████╗ ██████╗  █████╗ ████████╗ ██████╗ ██████╗ ██╗   ██╗
██║     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
██║     ███████║██████╔╝██║   ██║██████╔╝███████║   ██║   ██║   ██║██████╔╝ ╚████╔╝ 
██║     ██╔══██║██╔══██╗██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝  
███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║   ██║   
╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
'''

ascii_art_inventory = r'''
  _____ _   ___      ________ _   _ _______ ____  _______     __
 |_   _| \ | \ \    / /  ____| \ | |__   __/ __ \|  __ \ \   / /
   | | |  \| |\ \  / /| |__  |  \| |  | | | |  | | |__) \ \_/ / 
   | | | . ` | \ \/ / |  __| | . ` |  | | | |  | |  _  / \   /  
  _| |_| |\  |  \  /  | |____| |\  |  | | | |__| | | \ \  | |   
 |_____|_| \_|   \/   |______|_| \_|  |_|  \____/|_|  \_\ |_|   
'''


# F00
def linear_congruential_generator(m: int, a: int, c: int, seed: int) -> Iterator[int]:
    x = seed
    while True:
        yield x
        x = (a * x + c) % m

def random(lower_limit: float, upper_limit: float) -> float:
    global gen, seed_random
    rand = lower_limit + (next(gen) % int((upper_limit - lower_limit) * 100)) / 100
    seed_random = (seed_random * 1103515245 + 12345) & 0x7fffffff
    return rand//1
# Initialize the generator outside the function
seed_random = int(os.getpid() + time.time())
gen = linear_congruential_generator(m=2**31, a=1103515245, c=12345, seed=seed_random)

# validasi input
def my_isdigit(a): # Ini kode untuk mengecek apakah input berupa integer
    if not a: # Jaga-jaga nilai kosong
        return False
    
    for char in a:
        if char < '0' or char > '9':
            return False
    return True
    
def validate_integer_input(prompt):
    while True:
        value = input(prompt)
        if my_isdigit(value)==True:
            value = int(value)
            if value > 0:
                return value
            else:
                print("Input harus berupa Integer lebih dari 0. Coba lagi.")
        else:
            print("Input harus berupa Integer lebih dari 0. Coba lagi.") 

def validate_integer_input_2(n,prompt):
    while True:
        value = input(prompt)
        if my_isdigit(value)==True:
            value = int(value)
            if value > 0 and value <= n:
                return value
            else:
                print("Input harus sesuai. Coba lagi.")
        else:
            print("Input harus sesuai. Coba lagi.")
            
def validate_alpha_input(prompt):
    while True:
        value = input(prompt)
        if all('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in value):
            return value
        else:
            print("Input invalid! Input berupa alphabet, silahkan coba lagi")
            

# F14 - Load

def animate():
#prosedure untuk menampilkan animasi loading pada terminal
    for i in range (11):
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
    sys.stdout.write('\rSelesai!     ')
    print(" ")

def load (): #fungsi untuk memvalidasi apakah folder yang diberikan pengguna ada, dan mengopen file csv jika 
    #folder memang ada 
    parser=argparse.ArgumentParser(usage="")
    parser.add_argument("namafolder",nargs='?',help="Nama folder di dalam parent 'data' ")
    args=parser.parse_args()
    animate() #program menampilkan animasi loading 
    if args.namafolder is None: #nama folder tidak diberikan
        print("Tidak ada nama folder yang diberikan!")
        sys.exit()
    folder_path= os.path.join("data",args.namafolder)
    if (os.path.exists(folder_path)): #folder ada di directory
        #program selanjutnya membuka file csv yang ada pada folder dan mengubah ke dictionary
        with open (os.path.join("data",args.namafolder,"user.csv"),'r') as file :
            user=dictionary_csv("user.csv",args.namafolder)
        with open (os.path.join("data",args.namafolder,"monster.csv"),'r') as file :
            monster=dictionary_csv("monster.csv",args.namafolder)
        with open (os.path.join("data",args.namafolder,"monster_shop.csv"),'r') as file :
            monster_shop=dictionary_csv("monster_shop.csv",args.namafolder)
        with open (os.path.join("data",args.namafolder,"monster_inventory.csv"),'r') as file :
            monster_inventory=dictionary_csv("monster_inventory.csv",args.namafolder)
        with open (os.path.join("data",args.namafolder,"item_shop.csv"),'r') as file :
            item_shop=dictionary_csv("item_shop.csv",args.namafolder)
        with open (os.path.join("data",args.namafolder,"item_inventory.csv"),'r') as file :
            item_inventory=dictionary_csv("item_inventory.csv",args.namafolder)
        sambutan()
        return user,monster,monster_shop,monster_inventory,item_shop,item_inventory,True
        #fungsi memberikan keluaran berupa dictionary dari beberapa file csv yang telah diubah     
        
    else : #jika nama folder sudah diberikan tapi tidak ditemukan
        print (f"folder {args.namafolder} tidak ditemukan")
        return False

def fungsisplit(bariscsv):
     fields=[] #inisialisasi list kosong
     field='' #inisialisasi string kosong
     for baris in bariscsv: #loop melalui setiap baris pada csv
        for karakter in baris: #loop melalui setiap karakter pada baris 
            if karakter==';':  # Jika karakter adalah titik koma, tambahkan field saat ini ke dalam list fields
                fields.append(field) 
                field=''
            else:
                field+=karakter  # Tambahkan karakter ke dalam field saat ini
        if field.endswith('\n'):
            field=field[:-1]  # Jika field berakhir dengan newline, hilangkan newline tersebut
        fields.append(field)
        field=''
     return fields

def dictionary_csv(file_csv,nama_folder): #fungsi untuk mengubah csv ke dictionary
    csv=open(os.path.join("data", nama_folder,file_csv)) #buka file csv
    if file_csv =="user.csv" or file_csv=="monster.csv": 
        array_test=[i for i in csv]
        array_csv=fungsisplit(array_test)[5:] #ubah csv ke list dengan menghilangkan header
        header=fungsisplit(array_test)[:5] #simpan header dari csv tersebut
        data=[array_csv[i:i+5] for i in range (0,len(array_csv),5)] #memecah array_csv menjadi 5 bagian
        array_final={} #inisialisasi
        for i in header: #iterasi setiap elemen pada header
            # Membuat entri dalam dictionary array_final dengan nama kolom sebagai kunci
            array_final[i]=[ j[header.index(i)] for j in data]
    else: #perintah yang akan dilakukan jika file csv selain 'user.csv' dan 'monster.csv'
        array_test=[i for i in csv]
        array_csv=fungsisplit(array_test)[3:]
        header=fungsisplit(array_test)[:3]
        data=[array_csv[i:i+3] for i in range (0,len(array_csv),3)]
        array_final={}
        for i in header:
            array_final[i]=[j[header.index(i)] for j in data]

    return array_final

def sambutan():
    print(r"""
  _____        ______    _    
 / _ \ \      / / ___|  / \   
| | | \ \ /\ / / |     / _ \  
| |_| |\ V  V /| |___ / ___ \ 
 \___/  \_/\_/  \____/_/   \_\
          
  selamat datang di OWCA!!     
          
          """)

# F15 - Save

def save(user,monster,monster_shop,monster_inventory,item_shop,item_inventory):
    #menyimpan semua data ke csv
    nama_folder=input("Masukkan nama folder:") #fungsi meminta input nama folder
    path=os.path.join("data",nama_folder)
    if not os.path.exists(path):
        print(f"membuat folder data {nama_folder}")
    animate_saving(nama_folder)
    if not os.path.exists(path): # jika nama folder belum ada, maka buat folder baru
        os.mkdir(path)
    makecsvfile(nama_folder,user,"user.csv") #simpan semua data dalam bentuk csv ke folder tersebut
    makecsvfile(nama_folder,monster,"monster.csv")
    makecsvfile(nama_folder,monster_shop,"monster_shop.csv")
    makecsvfile(nama_folder,monster_inventory,"monster_inventory.csv")
    makecsvfile(nama_folder,item_shop,"item_shop.csv")
    makecsvfile(nama_folder,item_inventory,"item_inventory.csv")
    
def dicttocsv(dict): #fungsi yang mengubah dictionary ke csv
    dict_csv=[i for i in list(dict.keys())] #isi list awal dengan keys dari dictionary
    #list yang menyimpan seluruh komponnen (keys dan values) dari dictionary

    for i in range(int(len(list(dict[dict_csv[0]])))):
        for j in list(dict.keys()):
            dict_csv.append(dict[j][i]) #isi list dengan values dari dictionary secara bergantian berdasarkan keys
    field='' #inisiasi string kosong
    fields=[] #inisiasi array kosong
    if int(len(list(dict.keys())))==5: #mengubah list biasa menjadi list berbentuk seperti struktur data csv
        for i in range (0,len(dict_csv),5): #perulangan dengan kelipatan lima dari 0 sampai jumlah seluruh elemen list
            for j in range(i,i+5): #perulangan sebanyak lima kali 
                field+=dict_csv[j] #tambahkan setiap elemen list ke variabel string
                field+=';' #tambahkan ';' setiap akhir elemen untuk digunakan pada fungsi makecsvfile
            field+='\n' #tulis'\n' setiap akhir kelipatan lima untuk digunakan pada fungsi makecsvfile
            fields.append(field) #tambahkan nilai pada variabel field ke array fields
            field=''
    else: #perintah yang dilakukan untuk data yang keys nya 3 (selain user dan monster)
        for i in range (0,len(dict_csv),3):
            for j in range(i,i+3):
                field+=dict_csv[j]
                field+=';'
            field=field[:-1]+'\n'
            fields.append(field)
            field=''
    return fields            

def makecsvfile(nama_folder,dictionary,nama_file): #fungsi yang menulis csv pada suatu folder
    folder_path = os.path.join("data", nama_folder)
    if os.path.exists(folder_path):
        csv = dicttocsv(dictionary)
        with open(os.path.join("data", nama_folder, nama_file), 'w') as f:
            field = ''
            for i in csv:
                for idx in range(len(i)):
                    if i[idx] == ';':
                        f.write(field)
                        # Only write semicolon if the next character is not a newline
                        if idx + 1 < len(i) and i[idx + 1] != '\n':
                            f.write(';')
                        field = ''
                    elif i[idx] == '\n':
                        f.write(field)
                        f.write('\n')
                        field = ''
                    else:
                        field += i[idx]

def animate_saving(a): #fungsi untuk menampilkan animasi saving
    text = "Saving"
    max_dots = 5
    iterations = 2
    for _ in range(iterations):
        for i in range(max_dots + 1):
            sys.stdout.write("\r" + text + "." * i)
            sys.stdout.flush()
            time.sleep(0.5)
        
        sys.stdout.write("\r" + text + " " * max_dots)
        sys.stdout.flush()
        time.sleep(0.5)

    print(f"\nBerhasil menyimpan data di folder {a}")

# F16 - Exit

#fungsi untuk keluar dari program
def exit_game(user,monster,monster_shop,monster_inventory,item_shop,item_inventory):
    exit=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") #fungsi akan meminta input 
    while True: #perulangan diperlukan untuk mengecek apakah input dari pengguna valid
        if exit=="Y" or exit=="y": #pegguna ingin menyimpan file ditandai dengan string 'Y' atau 'y'
            save(user,monster,monster_inventory,monster_shop,item_inventory,item_shop) #jalankan fungsi save untuk menyimpan data
            print("Anda telah keluar dari permainan") #fungsi memberikan informasi
            break #hentikan perulangan karena semua langkah langkah telah dilakukan 
        elif exit=="N" or exit=="n": #pengguna ingin keluar tetapi tidak ingin menyimpan perubahan
            print("Data tidak disimpan") #fungsi memberikan informasi 
            print("Anda telah keluar dari permainan")
            break #hentikan perulangan karena semua langkah langkah telah dilakukan
        else: exit=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
            #perintah yang dilakukan ketika pengguna memasukan nilai yang tidak sesuai

user_info,monster,monster_shop,monster_inventory,potion_shop,item_inventory, valid=load()

# F01 - Register        
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
            return (str(len(user_info['id'])+1)), username, password, choice
        
        # Register a new user and append them to the existing user data


# Print the updated user data

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
    

# F03 - Logout
def logout(masuk: bool):
    if masuk:
        print("Logout Berhasil.")
    else:
        print("Logout gagal!")
        print("Anda belum login")

# F04 - Help

def help_before_login():
    print("=========== HELP ===========")
    print("Login belum dilakukan,silahkan login terlebih dahulu.")
    print("1. Login: Masuk ke dalam akun yang sudah terdaftar")
    print("2. Register: Membuat akun baru")

    print("\nFootnote:")
    print("Silahkan masukan fungsi yang terdaftar dalam menggunakan aplikasi")
    print("Pastikan input yang dimasukkan valid")

        
def help_admin():
    print("=========== HELP ===========")
    print("Selamat datang, Admin. Berikut adalah hal- hal yang dapat kamu lakukan:")
    print("1. Logout: Keluar dari akun yang sedang digunakan")
    print("2. Shop Management: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
    print("3. Monster Management: Melakukan manajemen Monster")
    print("4. Save: Menyimpan progress Anda")
    print("5. Exit: Keluar dari game")

    print("\nFootnote:")
    print("Silahkan masukan fungsi yang terdaftar dalam menggunakan aplikasi")
    print("Pastikan input yang dimasukkan valid")
        
def help_agent(username: str):
    print("=========== HELP ===========")
    print(f"Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
    print("1.  Logout: Keluar dari akun yang sedang digunakan")
    print("2.  Inventory: Melihat owca-dex yang dimiliki oleh Agent")
    print("3.  Shop: Membeli potion atau monster")
    print("4.  Battle: Bertarung melawan monster!")
    print("5.  Arena: Latih dan tingkatkan kemampuan agen dan para monstermu!")
    print("6.  Laboratory: Upgrade monster yang kamu miliki")
    print("7.  Save: Menyimpan progress Anda")
    print("8.  Exit: Keluar dari game")

    print("\nFootnote:")
    print("Silahkan masukan fungsi yang terdaftar dalam menggunakan aplikasi")
    print("Pastikan input yang dimasukkan valid")
def menu():
    print("""
        ====================== KOTA MONSTERTOPIA  ========================
      || ----------------------------------------------------------- ||
      ||              Selamat datang di kota MonsterTopia            ||
      ||                                                             ||
      ||    ~~ mulai petualangan dan kalahkan musuh musuh       ~~   ||
      ||                                                             ||
        =============================================================
          
                    (Ketik HELP untuk mendapat bantuan) 
          

""")

# F05 - Monster

def ListToDict_monster(monster_list):
    dictOfDict = {}
    for i in range(len(monster_list['id'])):
        monster_dict = {}
        monster_dict['Name'] = monster_list['type'][i]
        monster_dict['ATK Power'] = int(monster_list['atk_power'][i])
        monster_dict['DEF Power'] = int(monster_list['def_power'][i])
        monster_dict['HP'] = int(monster_list['hp'][i])
        monster_dict['MaxHP'] = int(monster_list['hp'][i])
        monster_dict['Level'] = 1
        dictOfDict[monster_list['id'][i]] = monster_dict
    return dictOfDict

def create_monster(monster, lvl):
    name = monster['Name']
    attack = monster['ATK Power']
    defense = monster['DEF Power']
    hp = monster['HP']
    level = int(lvl)
    wild_monster = {
            'Name' : name,
            'ATK Power': attack * (1 + ((level - 1) * 0.1)),
            'DEF Power': defense * (1 + ((level - 1) * 0.1)),
            'HP': hp * (1 + ((level - 1) * 0.1)),
            'MaxHP': hp * (1 + ((level - 1) * 0.1)),
            'Level': level,
        }
    return wild_monster

# F06 - Potion
def take_potion(monster, potion):
    if potion == 'Strength Potion':
        monster['ATK Power'] *= 1.05
    elif potion == 'Resilience Potion':
        monster['DEF Power'] *= 1.05
    elif potion == 'Healing Potion':
        monster['HP'] += 0.25 * monster['MaxHP']
        if monster['HP'] > monster['MaxHP']:
            monster['HP'] = monster['MaxHP']

# F07 - Inventory
def organize_user_info(user_info):
    user_data = {}
    for i in range(len(user_info['id'])):
        user_id = user_info['id'][i]
        username = user_info['username'][i]
        password = user_info['password'][i]
        role = user_info['role'][i]
        oc = user_info['oc'][i]
        user_data[user_id] = {
            'username': username,
            'password': password,
            'role': role,
            'oc': oc
        }
    return user_data

def ListToList_monster_inventory(monster_inventory):
    user_monsters = {}
    for i in range(len(monster_inventory['user_id'])):
        user_id = monster_inventory['user_id'][i]
        monster_id = monster_inventory['monster_id'][i]
        level = monster_inventory['level'][i]
        if user_id not in user_monsters:
            user_monsters[user_id] = []
        user_monsters[user_id].append({'monster_id': monster_id, 'level': level})
    return user_monsters

def ListToList_item_inventory(item_inventory):
    user_items = {}
    for i in range(len(item_inventory['user_id'])):
        user_id = item_inventory['user_id'][i]
        item_type = item_inventory['type'][i]
        quantity = item_inventory['quantity'][i]
        if user_id not in user_items:
            user_items[user_id] = []
        user_items[user_id].append({'type': item_type, 'quantity': quantity})
    return user_items

monster_dict = ListToDict_monster(monster)

def inventory(user, list_item, list_mons, id):
    global monster_dict
    list_of_inv = [i for i in range(4)]
    list_of_inv[0] = int(user[id]['oc'])

    list_of_inv_mons = []
    if id in monster_inventory['user_id']:
        list_of_inv_mons = [i for i in range(len(list_mons[id]))]
        for i in range(len(list_mons[id])):
            list_of_inv_mons[i] = create_monster(monster_dict[list_mons[id][i]['monster_id']], list_mons[id][i]['level'])
    list_of_inv[1] = list_of_inv_mons

    list_of_inv_item = [{'type': 'strength', 'quantity': 0}, {'type': 'resilience', 'quantity': 0}, {'type': 'healing', 'quantity': 0}]
    if id in item_inventory['user_id']:
        for i in range(len(list_item[id])):
            for j in range(3):
                if list_item[id][i]['type'] == list_of_inv_item[j]['type']:
                    list_of_inv_item[j]['quantity'] = int(list_item[id][i]['quantity'])
    list_of_inv[2] = list_of_inv_item
    list_of_inv[3] = id
    return(list_of_inv)

def show_detail_inventory(inventory):
    list_everything = [i for i in range(len(inventory[1])+(len(inventory[2]))+1)]
    list_everything[0] = inventory[0]
    for i in range(len(inventory[1])):
        list_everything[i+1] = inventory[1][i]
    for j in range(len(inventory[2])):
        list_everything[j+len(inventory[1])+1] = inventory[2][j]
    count = 1

    print(f'you have {list_everything[0]} coins') #print coins
    for i in range(1,len(list_everything)):
        if len(list_everything[i]) == 6:
            print(f'{count}. Monster       (Name: {list_everything[i]['Name']}, Lvl: {list_everything[i]['Level']}, HP: {list_everything[i]['HP']})')
        if len(list_everything[i]) == 2 and list_everything[i]['quantity'] != 0:
            print(f'{count}. Potion        (Type: {list_everything[i]['type']}, Qty: {list_everything[i]['quantity']})')
        count += 1
    
    index = validate_integer_input_2(len(list_everything)-1,'Index: ') 

    if len(list_everything[index]) == 6:
        print('Monster')
        print(f"Name      : {list_everything[index]['Name']}")
        print(f"ATK Power : {list_everything[index]['ATK Power']}")
        print(f"DEF Power : {list_everything[index]['DEF Power']}")
        print(f"HP        : {list_everything[index]['HP']}")
        print(f"Level     : {list_everything[index]['Level']}")
    elif len(list_everything[index]) == 2:
        print('Potion')
        print(f"Type      : {list_everything[index]['type']}")
        print(f"Quantity  : {list_everything[index]['quantity']}")
    return

def inventory_to_info(inv_player):
    user_info['oc'][int(inv_player[3])-1] = str(int(inv_player[0]))
    ind = []
    for i in range(len(item_inventory['user_id'])):
        if item_inventory['user_id'][i] == str(inv_player[3]) :
            ind.append(i)
    for j in range(len(ind)):
        for k in range(len(inv_player[2])):
            if item_inventory['type'][ind[j]] == inv_player[2][k]['type']:
                item_inventory['quantity'][ind[j]] = inv_player[2][k]['quantity']

# F08 - Battle
def take_damage(monster, damage):
    monster['HP'] -= damage
    if monster['HP'] < 0:
        monster['HP'] = 0

def attack_opponent(attacker, opponent):
    damage = attacker['ATK Power'] * ((random(7, 14)) / 10) * (1 - (opponent['DEF Power'] / 100))
    take_damage(opponent, damage)
    print(f"{attacker['Name']} menyerang {opponent['Name']} dan melakukan {damage} damage!")
    return damage

def is_alive(monster):
    return monster['HP'] > 0

def battle(inventory, monster_dict):
    wild_monster = monster_dict[str(int(random(1,6)))]
    used_potion = [False, False, False]
    run_away = False
    turn = 1
    print(sprite_goblin)
    print(f"{wild_monster['Name']} liar muncul!\n")
    print(f'Name: {wild_monster['Name']} \nATK Power : {wild_monster['ATK Power']} \nDEF Power : {wild_monster['DEF Power']} \nHP        : {wild_monster['HP']} \nLevel     : {wild_monster['Level']}\n')
    print('==== MONSTER LIST ====')
    for i in range(len(inventory[1])):
        print(f'{i+1}. {inventory[1][i]['Name']}')
    print()

    chosen_monster = validate_integer_input_2(len(inventory[1]), 'Pilih Monster: ')
    monster = inventory[1][int(chosen_monster)-1]
    monster['HP'] = monster['MaxHP']
    print(sprite_monster)
    print(f'Agen memilih {monster['Name']}\n')
    print(f'Name: {monster['Name']} \nATK Power : {monster['ATK Power']} \nDEF Power : {monster['DEF Power']} \nHP        : {monster['HP']} \nLevel     : {monster['Level']}\n')

    while is_alive(monster) and is_alive(wild_monster):
        print(f'==== TURN {turn} {monster['Name']} ====')
        print('1. Attack \n2. Use potion \n3. Quit')
        action = str(validate_integer_input_2(3, 'Pilih Perintah: '))

        if action == '1':
            attack_opponent(monster,wild_monster)
            print(f'Name: {wild_monster['Name']} \nATK Power : {wild_monster['ATK Power']} \nDEF Power : {wild_monster['DEF Power']} \nHP        : {wild_monster['HP']} \nLevel     : {wild_monster['Level']}\n')

        if action == '2':
            print(f'==== POTION LIST ==== \n1. Strength Potion (Qty: {inventory[2][0]['quantity']})- menambah ATK Power \n2. Resilience Potion (Qty: {inventory[2][1]['quantity']}) - menambah Power \n3. Healing Potion (Qty: {inventory[2][2]['quantity']}) - menambah Health')
            potion = str(validate_integer_input_2(3, 'Pilih Perintah: '))
            if potion == '1' and inventory[2][0]['quantity'] != 0 and used_potion[0] == False:
                take_potion(monster, 'Strength Potion')
                inventory[2][0]['quantity'] -= 1
                used_potion[0] = True
                print(f'{monster['Name']} menjadi lebih kuat')
            elif potion == '2' and inventory[2][1]['quantity'] != 0 and used_potion[1] == False:
                take_potion(monster, 'Resilience Potion')
                inventory[2][1]['quantity'] -= 1
                used_potion[1] = True
                print(f'{monster['Name']} menjadi kebal')
            elif potion == '3' and inventory[2][2]['quantity'] != 0 and used_potion[2] == False:
                take_potion(monster, 'Healing Potion')
                inventory[2][2]['quantity'] -= 1
                used_potion[2] = True
                print(f'{monster['Name']} menjadi sembuh')
            else:
                print('Potion habis!')

        if action == '3':
            success = random(0,2)
            if success == 1:
                print('Anda berhasil melarikan diri!')
                run_away = True
                break
            else: 
                print('Anda tidak berhasil melarikan diri!')
                
        if is_alive(wild_monster):
            print(f'==== TURN {turn} {wild_monster['Name']} ====')
            attack_opponent(wild_monster,monster)
            print(f'Name: {monster['Name']} \nATK Power : {monster['ATK Power']} \nDEF Power : {monster['DEF Power']} \nHP        : {monster['HP']} \nLevel     : {monster['Level']}\n')

        turn += 1
    if is_alive(monster) and not run_away:
        print(f"{monster['Name']} menang!")
        print(f'Name: {wild_monster['Name']} \nATK Power : {wild_monster['ATK Power']} \nDEF Power : {wild_monster['DEF Power']} \nHP        : {wild_monster['HP']} \nLevel     : {wild_monster['Level']}\n')
        coin_gain = random(5,31)
        inventory[0] += coin_gain
        print(f'Congrats, Anda mendapat {coin_gain} coins!')
    elif not run_away:
        print(f"{wild_monster['Name']} menang!")
        print(f'Name: {monster['Name']} \nATK Power : {monster['ATK Power']} \nDEF Power : {monster['DEF Power']} \nHP        : {monster['HP']} \nLevel     : {monster['Level']}\n')
        coin_gain = random(5,31)
        inventory[0] -= coin_gain
        if inventory[0]< 0:
            inventory[0] = 0
        print(f'Anda pingsan, Anda kehilangan {coin_gain} coins...')
    return inventory

# F09 - Arena
def arena(inventory, monster_dict):
    used_potion = [False, False, False]
    run_away = False
    turn = 1
    stage = 1
    total_damage = 0
    total_received = 0
    print('==== MONSTER LIST ====')
    for i in range(len(inventory[1])):
        print(f'{i+1}. {inventory[1][i]['Name']}')
    print()

    chosen_monster = validate_integer_input_2(len(inventory[2]), 'Pilih Monster: ')
    monster = inventory[1][int(chosen_monster)-1]
    monster['HP'] = monster['MaxHP']
    print(sprite_monster)
    print(f'Agen memilih {monster['Name']}\n')
    print(f'Name: {monster['Name']} \nATK Power : {monster['ATK Power']} \nDEF Power : {monster['DEF Power']} \nHP        : {monster['HP']} \nLevel     : {monster['Level']}\n')

    while stage < 6 and is_alive(monster) and not run_away:
        print(f'==== STAGE {stage} ====')
        wild_monster = monster_dict[str(int(random(1,6)))]
        wild_monster = create_monster(wild_monster, stage)
        monster['HP'] = monster['MaxHP']
        wild_monster['HP'] = wild_monster['MaxHP']
        print(sprite_goblin)
        print(f"A {wild_monster['Name']} liar muncul!\n")
        print(f'Name: {wild_monster['Name']} \nATK Power : {wild_monster['ATK Power']} \nDEF Power : {wild_monster['DEF Power']} \nHP        : {wild_monster['HP']} \nLevel     : {wild_monster['Level']}\n')
        
        while is_alive(monster) and is_alive(wild_monster):
            print(f'==== TURN {turn} {monster['Name']} ====')
            print('1. Attack \n2. Use potion \n3. Quit')
            action = str(validate_integer_input_2(3, 'Pilih Perintah: '))

            if action == '1':
                total_damage += attack_opponent(monster,wild_monster)
                print(f'Name: {wild_monster['Name']} \nATK Power : {wild_monster['ATK Power']} \nDEF Power : {wild_monster['DEF Power']} \nHP        : {wild_monster['HP']} \nLevel     : {wild_monster['Level']}\n')

            if action == '2':
                print(f'==== POTION LIST ==== \n1. Strength Potion (Qty: {inventory[2][0]['quantity']})- menambah ATK Power \n2. Resilience Potion (Qty: {inventory[2][1]['quantity']}) - menambah DEF Power \n3. Healing Potion (Qty: {inventory[2][2]['quantity']}) - menambah Health')
                potion = str(validate_integer_input_2(3, 'Pilih Perintah: '))
                if potion == '1' and inventory[2][0]['quantity'] != 0 and used_potion[0] == False:
                    take_potion(monster, 'Strength Potion')
                    inventory[2][0]['quantity'] -= 1
                    used_potion[0] = True
                    print(f'{monster['Name']} menjadi lebih kuat')
                elif potion == '2' and inventory[2][1]['quantity'] != 0 and used_potion[1] == False:
                    take_potion(monster, 'Resilience Potion')
                    inventory[2][1]['quantity'] -= 1
                    used_potion[1] = True
                    print(f'{monster['Name']} menjadi kebal')
                elif potion == '3' and inventory[2][2]['quantity'] != 0 and used_potion[2] == False:
                    take_potion(monster, 'Healing Potion')
                    inventory[2][2]['quantity'] -= 1
                    used_potion[2] = True
                    print(f'{monster['Name']} telah sembuh')
                else:
                    print('Potion habis!')

            if action == '3':
                success = random(0,2)
                if success == 1:
                    print('Anda berhasil melarikan diri!')
                    run_away = True
                    break
                else: 
                    print('Anda tidak berhasil melarikan diri!')
                    
            if is_alive(wild_monster):
                print(f'==== TURN {turn} {wild_monster['Name']} ====')
                total_received += attack_opponent(wild_monster,monster)
                print(f'Name: {monster['Name']} \nATK Power : {monster['ATK Power']} \nDEF Power : {monster['DEF Power']} \nHP        : {monster['HP']} \nLevel     : {monster['Level']}\n')
            turn += 1
        
        if is_alive(monster) and not run_away:
            print(f"{monster['Name']} menang!")
            print(f'Name: {wild_monster['Name']} \nATK Power : {wild_monster['ATK Power']} \nDEF Power : {wild_monster['DEF Power']} \nHP        : {wild_monster['HP']} \nLevel     : {wild_monster['Level']}\n')
            stage += 1
        elif not run_away:
            print(f"{wild_monster['Name']} menang!")
            print(f'Name: {wild_monster['Name']} \nATK Power : {wild_monster['ATK Power']} \nDEF Power : {wild_monster['DEF Power']} \nHP        : {wild_monster['HP']} \nLevel     : {wild_monster['Level']}\n')    

    inventory[0] += (30*(stage-1))
    print('==== STATS ====')
    print(f'Total hadiah      : {(30*(stage-1))} OC \nJumlah stage      : {stage-1} \nDamage diberikan  : {total_damage} \nDamage diterima   : {total_received}')
    return inventory

# Example usage:

sprite_goblin = r'''       

           _/\----/\   
          /         \     /\
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \  |  |
        /   `^^^^^'    \ |  |
      ./  /|            \|  |_
     /   / |         |\__     /
     \  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__

'''

sprite2_cat = r'''

        |\      _,,,---,,_
    ZZZzz /,`.-'`'    -.  ;-;;,_
        |,4-  ) )-,_. ,\ (  `'-'
        '---''(_/--'  `-'\_)  

'''
sprite_monster = r'''
          /\----/\_   
         /         \   /|
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \  |   |   |
         |  |   |   |
          \._\   \._\ 
'''

# F10 - Shop & Currency
# Global variables for currency and inventory

monsters = [{'id': monster_shop['monster_id'][i], 'stock': int(monster_shop['stock'][i]), 'price': int(monster_shop['price'][i]), 'type': monster['type'][i], 'atk_power': int(monster['atk_power'][i]), 'def_power': int(monster['def_power'][i]), 'hp': int(monster['hp'][i])} for i in range(len(monster_shop['monster_id']))]
potions = [{'type': potion_shop['type'][i], 'stock': int(potion_shop['stock'][i]), 'price': int(potion_shop['price'][i])} for i in range(len(potion_shop['type']))]

def spend_currency(inventory, amount):
    if inventory[0] >= amount:
        inventory[0] -= amount
        return True
    else:
        print("OC anda tidak cukup.")
        return False

def buy_item(item_type, item_id, inventory, quantity=1):
    if item_type == "monster":
        # Search for a monster with the given item_id
        item = None
        for monster in monsters:
            if monster['id'] == item_id:
                item = monster
                break
        if not item:
            print("Monster dengan ID tersebut tidak ada.")
            return
        if item['stock'] < quantity:
            print("Stok monster tidak mencukupi.")
            return
        price = item['price'] * quantity
        if not spend_currency(inventory, price):
            return
        if any(monster['Name'] == item['type'] for monster in inventory[1]):
            print("Monster tersebut sudah ada dalam inventory-mu!")
            return
        item['stock'] -= quantity
        new_monster = {'Name': item['type'], 'ATK Power': item['atk_power'], 'DEF Power': item['def_power'], 'HP': item['hp'], 'MaxHP': item['hp'], 'Level': 1}
        inventory[1].append(new_monster)
        print(f"Berhasil membeli item: Monster {new_monster['Name']}. Item sudah masuk ke inventory-mu!")
    elif item_type == "potion":
        item = None
        for potion in potions:
            if potion['type'] == item_id:
                item = potion
                break
        if not item:
            print("Potion dengan ID tersebut tidak ada.")
            return
        if item['stock'] < quantity:
            print("Stok potion tidak mencukupi.")
            return
        price = item['price'] * quantity
        if not spend_currency(inventory, price):
            return
        item['stock'] -= quantity
        for inv_item in inventory[2]:
            if inv_item['type'] == item_id:
                inv_item['quantity'] += quantity
                break
        else:
            inventory[2].append({'type': item_id, 'quantity': quantity})
        print(f"Berhasil membeli item: Potion {item_id}. Item sudah masuk ke inventory-mu!")

def display_shop(inventory):
    print("Irasshaimase! Selamat datang di SHOP!!\n")
    while True:
        print(">>> Pilih aksi (lihat/beli/keluar):")
        action = input()
        if action == "lihat":
            print(">>> Mau lihat apa? (monster/potion):")
            item_type = input()
            if item_type == "monster":
                print(f"{'ID':<3} | {'Type':<10} | {'ATK Power':<9} | {'DEF Power':<9} | {'HP':<4} | {'Stock':<5} | {'Price':<6}")
                print("-" * 61)
                for monster in monsters:
                    print(f"{monster['id']:<3} | {monster['type']:<10} | {monster['atk_power']:<9} | {monster['def_power']:<9} | {monster['hp']:<4} | {monster['stock']:<5} | {monster['price']:<6}")
            elif item_type == "potion":
                print(f"{'Type':<10} | {'Stock':<5} | {'Price':<6}")
                print("-" * 23)
                for potion in potions:
                    print(f"{potion['type']:<10} | {potion['stock']:<5} | {potion['price']:<6}")
            else:
                print("Tipe item tidak valid.")
        elif action == "beli":
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {inventory[0]}.")
            print(">>> Mau beli apa? (monster/potion):")
            item_type = input()
            if item_type == "monster":
                print(">>> Masukkan ID monster:")
                item_id = input()
                print(">>> Masukkan jumlah:")
                quantity = int(input())
                buy_item("monster", item_id, inventory, quantity)
            elif item_type == "potion":
                print(">>> Masukkan type potion:")
                item_id = validate_alpha_input()
                print(">>> Masukkan jumlah:")
                quantity = validate_integer_input()
                buy_item("potion", item_id, inventory, quantity)
            else:
                print("Tipe item tidak valid.")
        elif action == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
            break
        else:
            print("Aksi tidak valid.")

# F11 - Laboratory
def get_value(dictionary, key, default=None):
    if key in dictionary:
        return dictionary[key]
    else:
        return default

def laboratory(inventory):
    # Konversi data monster dari dictionary ke list of tuples
    monsters = inventory[1]

    # Harga upgrade berdasarkan level
    upgrade_prices = {
        1: 300,
        2: 500,
        3: 800,
        4: 1000
    }

    def display_monsters(monsters):
        print("============= MONSTER LIST =============")
        for i in range(len(monsters)):
            monster = monsters[i]
            print(f"{i+1}. {monster['Name']} (Level: {monster['Level']})")

    def display_upgrade_prices(upgrade_prices):
        print("============= UPGRADE PRICE =============")
        for level, price in upgrade_prices.items():
            print(f"Level {level} -> Level {level + 1} : {price} OC")

    def choose_monster(monsters):
        print(">>> Pilih monster: ")
        choice = validate_integer_input("Masukkan nomor monster: ")
        choice = int(choice) - 1
        if 0 <= choice < len(monsters):
            return choice
        print("Pilihan tidak valid. Coba lagi.")
        return choose_monster(monsters)

    def upgrade_monster(monsters, index, upgrade_prices, oc_balance):
        monster = monsters[index]
        name, level = monster['Name'], monster['Level']
        if level >= 5:
            print(f"Maaf, monster yang Anda pilih sudah memiliki level maksimum.")
            return oc_balance
        
        upgrade_cost = get_value(upgrade_prices, level, 0)
        print(f"{name} akan di-upgrade ke level {level + 1}.")
        print(f"Harga untuk melakukan upgrade {name} adalah {upgrade_cost} OC.")
        print(">>> Lanjutkan upgrade (y/n): ")
        confirm = input()
        if confirm == 'y':
            if oc_balance >= upgrade_cost:
                oc_balance -= upgrade_cost
                inventory[1][index] = create_monster(monster_dict[str(index+1)], inventory[1][index]['Level']+1)
                print(f"Selamat, {name} berhasil di-upgrade ke level {level + 1}!")
                print(inventory)
            else:
                print("OC tidak cukup untuk melakukan upgrade.")
        else:
            print("Upgrade dibatalkan.")
        return oc_balance

    if len(inventory[1]) > 0:
        print("Selamat datang di Lab Dokter Asep !!!")
        display_monsters(monsters)
        display_upgrade_prices(upgrade_prices)
        
        index = choose_monster(monsters)
        oc_balance = upgrade_monster(monsters, index, upgrade_prices, inventory[0])
        inventory[0] = oc_balance
        
        print("OC Balance:", oc_balance)
        display_monsters(monsters)
        return inventory[0], inventory[1]
    else:
        print('Anda tidak memiliki monster, beli dulu di shop')
        return inventory[0], inventory[1]
# F12 - Shop Management

def ubahmonster(monster, monster_shop):
        match_monsters(monster, monster_shop)
        id = input("Masukkan id monster yang ingin diubah: ")
        if id in monster_shop["monster_id"]:
            index = monster_shop["monster_id"].index(id)
            harga = input("Masukkan harga monster baru: ")
            stok = input("Masukkan stok monster baru: ")
            monster_shop["price"][index] = harga
            monster_shop["stock"][index] = stok
            print("Monster berhasil dirubah!")
            match_monsters(monster, monster_shop)
        else:
            print("Monster tidak ditemukan!")

def remove_by_index(dictionary, key, index):
    dictionary[key] = dictionary[key][:index] + dictionary[key][index+1:]

def fungsisplit(bariscsv):
    fields=[] #inisialisasi list kosong
    field='' #inisialisasi string kosong
    for baris in bariscsv: #loop melalui setiap baris pada csv
        for karakter in baris: #loop melalui setiap karakter pada baris 
            if karakter==';':  # Jika karakter adalah titik koma, tambahkan field saat ini ke dalam list fields
                fields.append(field) 
                field=''
            else:
                field+=karakter  # Tambahkan karakter ke dalam field saat ini
        if field.endswith('\n'):
            field=field[:-1]  # Jika field berakhir dengan newline, hilangkan newline tersebut
        fields.append(field)
        field=''
    return fields

def ubah_potion(potion, potion_shop):
    match_items(potion, potion_shop)
    # Minta id potion dari user
    potion_id = int(input("Masukkan id potion: "))

    # Cek apakah id potion ada di potion
    if potion_id in potion['id']:
        # Dapatkan indeks dari id potion di potion
        indeks_potion = potion['id'].index(potion_id)

        # Cek apakah type potion ada di potion_shop
        if potion['type'][indeks_potion] in potion_shop['type']:
            # Dapatkan indeks dari type potion di potion_shop
            indeks_shop = potion_shop['type'].index(potion['type'][indeks_potion])

            # Minta stok dan harga baru dari user
            stok_baru = int(input("Masukkan stok baru: "))
            harga_baru = int(input("Masukkan harga baru: "))

            # Ubah stok dan harga potion di potion_shop
            potion_shop['stock'][indeks_shop] = stok_baru
            potion_shop['price'][indeks_shop] = harga_baru

            print(f"Stok dan harga {potion['type'][indeks_potion]} telah berhasil diubah!")
        else:
            print("Potion dengan type tersebut tidak ditemukan di shop!")
    else:
        print("Potion dengan id tersebut tidak ditemukan di potion!")

def hapus_potion(potion, potion_shop):
    # Minta id potion dari user
    potion_id = int(input("Masukkan id potion: "))

    # Cek apakah id potion ada di potion
    if potion_id in potion['id']:
        # Dapatkan indeks dari id potion di potion
        indeks_potion = potion['id'].index(potion_id)

        # Cek apakah type potion ada di potion_shop
        if potion['type'][indeks_potion] in potion_shop['type']:
            # Dapatkan indeks dari type potion di potion_shop
            indeks_shop = potion_shop['type'].index(potion['type'][indeks_potion])

            # Minta konfirmasi dari user untuk menghapus potion
            konfirmasi = input(f"Apakah anda yakin ingin menghapus {potion_shop['type'][indeks_shop]} dari shop (y/n)? ")
            if konfirmasi == 'y':
                # Hapus potion dari potion_shop
                remove_by_index(potion_shop, 'type', indeks_shop)
                remove_by_index(potion_shop, 'stock', indeks_shop)
                remove_by_index(potion_shop, 'price', indeks_shop)
                print(f"{potion['type'][indeks_potion]} telah berhasil dihapus dari shop!")
            else:
                print("Potion tidak dihapus.")
        else:
            print("Potion dengan type tersebut tidak ditemukan di potion_shop!")
    else:
        print("Potion dengan id tersebut tidak ditemukan di potion!")

def match_monsters(monster, monster_shop):
    # Print the table headers
    print(f'{"ID":<5} | {"Type":<20} | {"ATK Power":<10} | {"DEF Power":<10} | {"HP":<5} | {"Stock":<5} | {"Price":<5}')

    # Iterate over the monsters
    for i in range(len(monster['id'])):
        # Iterate over the monster_shop
        for j in range(len(monster_shop['monster_id'])):
            # If the ids match
            if monster['id'][i] == monster_shop['monster_id'][j]:
                # Print the monster data in a table format
                print(f'{monster["id"][i]:<5} | {monster["type"][i]:<20} | {monster["atk_power"][i]:<10} | {monster["def_power"][i]:<10} | {monster["hp"][i]:<5} | {monster_shop["stock"][j]:<5} | {monster_shop["price"][j]:<5}')
                # Stop iterating over the monster_shop
                break

def hapus_item(lst, index):
    removed_item = lst[index]
    lst = lst[:index] + lst[index+1:]
    return removed_item, lst

def match_items(item_inventory, item_shop):
    # Print the table headers
    print(f'{"ID":<5} | {"Type":<20} | {"Stok":<5} | {"Price":<5}')

    # Create a list to store the types that have been printed
    printed_types = []

    # Iterate over the items in the inventory
    for i in range(len(item_inventory['type'])):
        # If the type has already been printed, skip it
        if item_inventory['type'][i] in printed_types:
            continue

        # Iterate over the items in the shop
        for j in range(len(item_shop['type'])):
            # If the types match
            if item_inventory['type'][i] == item_shop['type'][j]:
                # Check if the index exists in item_shop
                if j < len(item_shop['stock']) and j < len(item_shop['price']):
                    # Print the item data in a table format
                    print(f'{item_inventory["id"][i]:<5} | {item_inventory["type"][i]:<20} | {item_shop["stock"][j]:<5} | {item_shop["price"][j]:<5}')
                    # Add the type to the list of printed types
                    printed_types.append(item_inventory['type'][i])
                    # Stop iterating over the item_shop
                    break

def tambah_monster(monster, monster_shop):
    # Print monster yang tersedia
    print_monster_tersedia(monster, monster_shop)

    # Minta id monster dari user
    monster_id = int(input("Masukkan id monster: "))

    # Cek apakah id monster ada di monster dan belum ada di monster_shop
    if monster_id in monster['monster_id'] and monster_id not in monster_shop['monster_id']:
        # Dapatkan indeks dari id monster di monster
        indeks_monster = monster['monster_id'].index(monster_id)

        # Minta stok dan harga awal dari user
        stok_awal = int(input("Masukkan stok awal: "))
        harga = int(input("Masukkan harga: "))

        # Tambahkan monster ke monster_shop
        monster_shop['monster_id'].append(monster_id)
        monster_shop['type'].append(monster['type'][indeks_monster])
        monster_shop['stock'].append(stok_awal)
        monster_shop['price'].append(harga)

        print(f"{monster['type'][indeks_monster]} telah berhasil ditambahkan ke dalam shop!")
    else:
        print("Monster dengan id tersebut tidak ditemukan di monster atau sudah ada di shop!")

def tambah_potion(potion, potion_shop):
    # Print potion yang tersedia
    print_potion_tersedia(potion, potion_shop)

    # Minta id potion dari user
    potion_id = int(input("Masukkan id potion: "))

    # Cek apakah id potion ada di potion dan belum ada di potion_shop
    if potion_id in potion['id'] and potion_id not in potion_shop['type']:
        # Dapatkan indeks dari id potion di potion
        indeks_potion = potion['id'].index(potion_id)

        # Minta stok dan harga awal dari user
        stok_awal = int(input("Masukkan stok awal: "))
        harga = int(input("Masukkan harga: "))

        # Tambahkan potion ke potion_shop
        potion_shop['type'].append(potion['type'][indeks_potion])
        potion_shop['stock'].append(stok_awal)
        potion_shop['price'].append(harga)

        print(f"{potion['type'][indeks_potion]} telah berhasil ditambahkan ke dalam shop!")
    else:
        print("Potion dengan id tersebut tidak ditemukan di potion atau sudah ada di shop!")

def print_monster_tersedia(monster, monster_shop):
    print("{:<10} | {:<15} | {:<10} | {:<10} | {:<10} |".format("ID", "Type", "ATK Power", "DEF Power", "HP"))
    for i in range(len(monster['id'])):
        if monster['id'][i] not in monster_shop['monster_id']:
            print("{:<10} | {:<15} | {:<10} | {:<10} | {:<10} |".format(monster['id'][i], monster['type'][i], monster['atk_power'][i], monster['def_power'][i], monster['hp'][i]))

def print_potion_tersedia(potion, item_shop):
    print("{:<10} | {:<15}".format("ID", "Type"))
    for i in range(len(potion['id'])):
        if potion['type'][i] not in item_shop['type']:
            print("{:<10} | {:<15}".format(potion['id'][i], potion['type'][i]))

def tambah_monster(monster, monster_shop):
    # Print monster yang tersedia
    print_monster_tersedia(monster, monster_shop)

    # Minta id monster dari user
    monster_id = input("Masukkan id monster: ")

    # Cek apakah id monster ada di monster dan belum ada di monster_shop
    if monster_id in monster['id'] and monster_id not in monster_shop['monster_id']:
        # Dapatkan indeks dari id monster di monster
        indeks_monster = monster['id'].index(monster_id)

        # Minta stok dan harga awal dari user
        stok_awal = int(input("Masukkan stok awal: "))
        harga = int(input("Masukkan harga: "))

        # Tambahkan monster ke monster_shop
        monster_shop['monster_id'].append(monster_id)
        monster_shop['stock'].append(stok_awal)
        monster_shop['price'].append(harga)

        print(f"{monster['type'][indeks_monster]} telah berhasil ditambahkan ke dalam shop!")
    else:
        print("Monster dengan id tersebut tidak ditemukan di monster atau sudah ada di shop!")

def hapus_monster(monster, monster_shop):
    match_monsters(monster, monster_shop)
    id_monster = input("Masukkan id monster yang ingin dihapus: ")
    if id_monster in monster_shop["monster_id"]:
        monster_type = monster['type'][monster['id'].index(id_monster)]
        confirmation = input(f"Apakah anda yakin ingin menghapus {monster_type}? (y/n): ")
        if confirmation.lower() == "y":
            index = monster_shop["monster_id"].index(id_monster)
            removed_item, monster_shop["monster_id"] = hapus_item(monster_shop["monster_id"], index)
            removed_item, monster_shop["price"] = hapus_item(monster_shop["price"], index)
            removed_item, monster_shop["stock"] = hapus_item(monster_shop["stock"], index)
            print((f"{monster_type} berhasil dihapus!"))
    else:
        print("Monster tidak ditemukan!")

potion = {
    'id': [1, 2, 3],
    'type': ['strength', 'resilience', 'healing']
}

ascii_art = r'''
  ____  _   _  ___  ____    __  __    _    _   _    _    ____ _____ __  __ _____ _   _ _____ 
 / ___|| | | |/ _ \|  _ \  |  \/  |  / \  | \ | |  / \  / ___| ____|  \/  | ____| \ | |_   _|
 \___ \| |_| | | | | |_) | | |\/| | / _ \ |  \| | / _ \| |  _|  _| | |\/| |  _| |  \| | | |  
  ___) |  _  | |_| |  __/  | |  | |/ ___ \| |\  |/ ___ \ |_| | |___| |  | | |___| |\  | | |  
 |____/|_| |_|\___/|_|     |_|  |_/_/   \_\_| \_/_/   \_\____|_____|_|  |_|_____|_| \_| |_|  
'''

# SHOP MANAGEMENT SYSTEM

def shop_management():
    print(ascii_art)
    while True:
        print("Selamat datang di Management SHOP, silahkan pilih menu yang diinginkan (lihat/tambah/ubah/hapus/keluar): ")
        aksi = input(">>> \033[1m Pilih Aksi : \033[0m",)
        
        while aksi not in ["lihat","tambah","ubah","hapus","keluar"]:
            print("Aksi yang dimasukkan tidak valid!")
            aksi = input(">>> \033[1m Pilih Aksi : \033[0m",)
        
        if aksi == "lihat":
            opsi_lihat = input("Mau lihat apa? (monster/potion): ")
            if opsi_lihat == "monster":
                match_monsters(monster, monster_shop)
            if opsi_lihat == "potion":
                match_items(potion, potion_shop)
            
        elif aksi == "tambah":
            opsi_tambah = input("Mau tambah apa? (monster/potion): ")
            if opsi_tambah == "monster":
                tambah_monster(monster, monster_shop)
            
            elif opsi_tambah == "potion":
                tambah_potion(potion, potion_shop)

        elif aksi == "ubah":
            opsi_ubah = input("Mau ubah apa? (monster/potion): ")
            if opsi_ubah == "monster":
                ubahmonster(monster, monster_shop)
            elif opsi_ubah == "potion":
                ubah_potion(potion,potion_shop)
                        
        elif aksi == "hapus":
            opsi_hapus = input("Mau hapus apa? (monster/potion): ")
            if opsi_hapus == "monster":
                hapus_monster(monster, monster_shop)
            if opsi_hapus == "potion":
                match_items(potion, potion_shop)
                hapus_potion(potion, potion_shop)
                
        elif aksi == "keluar":
            break
        
# F13 - Monster Management


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

def main():
    global item_inventory
    global monster_inventory
    global user_info
    global monsters
    global potions
    play = True
    while play:
        opsi = input('>>> ')
        if opsi == 'register':
            new_id, new_username, new_password, new_chosen_monster = register_account()
            user_info['id'].append(new_id)
            user_info['username'].append(new_username)
            user_info['password'].append(new_password)
            user_info['role'].append('agent')
            user_info['oc'].append('0')
            monster_inventory['user_id'].append(new_id)
            monster_inventory['monster_id'].append(str(new_chosen_monster))
            monster_inventory['level'].append('1')
        if opsi == 'login':
            id = str(login(user_info))
            if id != '-1':
                menu()
                user_info_org = organize_user_info(user_info)
                inventory_of_monsters = ListToList_monster_inventory(monster_inventory)
                inventory_of_items = ListToList_item_inventory(item_inventory)
                inv_player = inventory(user_info_org, inventory_of_items, inventory_of_monsters, (str(int(id)+1)))
                user_game = True
                while user_game:
                    option = input('>>> ')
                    if option == 'battle' or option == 'Battle' or option == 'BATTLE':
                        print(ascii_art_battle)
                        inv_player = battle(inv_player, monster_dict)
                        inventory_to_info(inv_player)
                    if option == 'arena' or option == 'Arena' or option == 'ARENA':
                        print(ascii_art_arena)
                        inv_player = arena(inv_player, monster_dict)
                        inventory_to_info(inv_player)
                    if option == 'inventory':
                        print(ascii_art_inventory)
                        show_detail_inventory(inv_player)
                    if option == 'shop':
                        print(ascii_art_shop)
                        monsters = [{'id': monster_shop['monster_id'][i], 'stock': int(monster_shop['stock'][i]), 'price': int(monster_shop['price'][i]), 'type': monster['type'][i], 'atk_power': int(monster['atk_power'][i]), 'def_power': int(monster['def_power'][i]), 'hp': int(monster['hp'][i])} for i in range(len(monster_shop['monster_id']))]
                        potions = [{'type': potion_shop['type'][i], 'stock': int(potion_shop['stock'][i]), 'price': int(potion_shop['price'][i])} for i in range(len(potion_shop['type']))]
                        display_shop(inv_player)
                    if option == 'laboratory':
                        print(ascii_art_laboratory)
                        inv_player[0], inv_player[1] = laboratory(inv_player)
                    if option == 'shop management':
                        if user_info['role'][int(id)] == 'admin':
                            shop_management()
                        else:
                            print('Anda bukan admin.')
                    if option == 'monster management':
                        if user_info['role'][int(id)] == 'admin':
                            monster_management()
                        else:
                            print('Anda bukan admin.')
                    if option == 'logout':
                        logout(True)
                        inventory_to_info(inv_player)
                        user_game = False
                        print('anda telah logout.')
                    if option == 'help':
                        if user_info['role'][int(id)] == 'admin':
                            help_admin()
                        else:
                            help_agent(user_info['username'][int(id)])
                    if option == 'save':
                        inventory_to_info(inv_player)
                        save(user_info,monster,monster_shop,monster_inventory,potion_shop,item_inventory)
                    if option == 'exit':
                        opsi = 'exit'
                        break
        if opsi == 'logout':
            logout(False)
        if opsi == 'help':
            help_before_login()
        if opsi == 'exit':
            exit_game(user_info,monster,monster_shop,monster_inventory,potion_shop,item_inventory)
            break
        
main()
