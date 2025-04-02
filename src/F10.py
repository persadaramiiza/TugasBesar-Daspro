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