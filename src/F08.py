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
