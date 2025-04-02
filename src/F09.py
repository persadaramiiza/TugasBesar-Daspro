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