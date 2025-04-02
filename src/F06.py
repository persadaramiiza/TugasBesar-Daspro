def take_potion(monster, potion):
    if potion == 'Strength Potion':
        monster['ATK Power'] *= 1.05
    elif potion == 'Resilience Potion':
        monster['DEF Power'] *= 1.05
    elif potion == 'Healing Potion':
        monster['HP'] += 0.25 * monster['MaxHP']
        if monster['HP'] > monster['MaxHP']:
            monster['HP'] = monster['MaxHP']
