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