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