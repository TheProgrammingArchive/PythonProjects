import random
tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tup2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tup3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
while True:
    money_Value = 0
    x = random.choice(tup1)
    y = random.choice(tup2)
    z = random.choice(tup3)
    if(x == y and y == z):
        print(x, y, z)
        print("You won!")
        money_Value = money_Value + 1000
        print(f"Balance = {money_Value}")
    else:
        print(x, y, z)
        print("You lost!")
    rep = input("Do you want to try again (Y/N): ")
    if(rep.upper() == 'N'):
        break


