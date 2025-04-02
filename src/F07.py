
def ListToList_monster_inventory(monster_inventory):
    user_monsters = {}
    for user_id, monster_id, level in zip(monster_inventory['user_id'], monster_inventory['monster_id'], monster_inventory['level']):
        if user_id not in user_monsters:
            user_monsters[user_id] = []
        user_monsters[user_id].append({'monster_id': monster_id, 'level': level})
    return user_monsters

def ListToList_item_inventory(item_inventory):
    user_items = {}
    for user_id, item_type, quantity in zip(item_inventory['user_id'], item_inventory['type'], item_inventory['quantity']):
        if user_id not in user_items:
            user_items[user_id] = []
        user_items[user_id].append({'type': item_type, 'quantity': quantity})
    return user_items

def organize_user_info(user_info):
    user_data = {}
    for id, username, password, role, oc in zip(user_info['id'], user_info['username'], user_info['password'], user_info['role'], user_info['oc']):
        user_data[id] = {
            'username': username,
            'password': password,
            'role': role,
            'oc': oc
        }
    return user_data

inventory_of_monsters = ListToList_monster_inventory(monster_inventory)
inventory_of_items = ListToList_item_inventory(item_inventory)
user_info_org = organize_user_info(user_info)

def inventory(user, list_item, list_mons, id):
    list_of_inv = [i for i in range(4)]
    list_of_inv[0] = int(user[id]['oc'])

    list_of_inv_mons = [i for i in range(len(list_mons[id]))]
    for i in range(len(list_mons[id])):
        list_of_inv_mons[i] = create_monster(monster_dict[list_mons[id][i]['monster_id']], list_mons[id][i]['level'])
    list_of_inv[1] = list_of_inv_mons

    list_of_inv_item = [{'type': 'strength', 'quantity': 0}, {'type': 'resilience', 'quantity': 0}, {'type': 'healing', 'quantity': 0}]
    for i in range(len(list_item[id])):
        for j in range(3):
            if list_item[id][i]['type'] == list_of_inv_item[j]['type']:
                list_of_inv_item[j]['quantity'] = int(list_item[id][i]['quantity'])
    list_of_inv[2] = list_of_inv_item
    list_of_inv[3] = id
    return(list_of_inv)

inv_player = inventory(user_info_org, inventory_of_items, inventory_of_monsters,'3')

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
        if len(list_everything[i]) == 2 and list_everything[i]['quantity'] != '0':
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
