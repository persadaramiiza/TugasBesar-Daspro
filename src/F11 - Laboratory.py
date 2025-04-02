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