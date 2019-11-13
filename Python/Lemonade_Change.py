
from typing import List



def lemonade_chnage(bills: List[int]) -> bool:
    bank = {'5':0, '10':0, '20':0}
    for b in bills:
        if b == 5:
            bank['5'] += 1
        elif b == 10:
            bank['10'] += 1
            bank['5'] -= 1
            if bank['5'] < 0:
                return False
        elif b == 20:
            bank['20'] += 1
            if bank['10'] > 0:
                bank['10'] -= 1
                bank['5'] -= 1
            else:
                bank['5'] -= 3
            if bank['10'] < 0 or bank['5'] < 0:
                return False
    return True





x = [5, 5, 5, 10, 20]
print(lemonade_chnage(x))

x = [5, 5, 10, 10, 20]
print(lemonade_chnage(x))