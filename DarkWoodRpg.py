import random as r

hp = 0
coins = 0
damage = 0

# инициализация жизней монет... далее формат строки по индексу
def printParameters():
    print('У тебя {0} жизней, {1} монет и {2} урона.'.format(hp, coins, damage)) 


def printHp():
    print('У тебя', hp, 'жизней')

def printCoins():
    print('У тебя', coins, 'монет')

def printDamage():
    print('У тебя', damage, 'урона')


# встретили магаз
def meetShop():
    global hp
    global coins
    global damage

    # поверка можем ли что нибудь купить
    # если стоимость больше чем монет то досвидос
    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            printCoins()
            return True
        print('Недостаточно золота!')
        return False
    
    # Уровень оружие. уровень дамага. 
    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 5) * weaponLvl
    # Список оружия, продающиеся в магазе
    weapon = ['Дробовик', 'Железный меч', 'Лопата', 'Перочинный нож', 'Лук', 'Бейсбольная бита']
    # Редкость оружия
    weaponRarities = ['Испорченый', 'Редкий', 'Легендарный']
    weaponRarity = weaponRarities[weaponLvl -1]
    # Стоимость оружия, рандомное значение умноженый на ур орижия
    weaponCost = r.randint(3, 10) * weaponLvl
    # оружие которое предложит торговец
    weapon = r.choice(weapon)
    
    oneHpCost = 5
    threeHpCost = 12

    print('Вы встретили торговца!')
    printParameters()

    while input('Что ты будешь делать(зайти/уйти):').lower()=='зайти':
        print('1) одна еденица здоровья -', oneHpCost, 'монет')
        print('2) три еденицы здоровья -', threeHpCost, 'монет')
        print('3) {0} {1} - {2} монет.'.format(weaponRarity, weapon, weaponCost))

        choice = input('Что будешь покупать? ')
        if choice == '1':
            if buy(oneHpCost):
                hp += 1
                printHp()
        elif choice == '2':
            if buy(threeHpCost):
                hp += 3
                printHp()
        elif choice == '3':
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
        else:
            print('Я такое не продаю!')


def meetMonster():
    global hp
    global coins

    monsterLvl = r.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsters = ["Жук-калоед", "Крыса", "Зомби", "Челмедведосвин", "Черт", "Паук-жнец"]

    monster = r.choice(monsters)

    print("Ты встретил монстра - {0}, у него {1} уровень, {2} жизней и {3} урона.".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParameters()

    while monsterHp > 0:
        choice = input("Что будешь делать (атака/бег): ").lower()

        if choice == "атака":
            monsterHp -= damage
            print("Ты ударим монстра и у него осталось", monsterHp, "жизней.")
        elif choice == "бег":
            chance = r.randint(0, monsterLvl)
            if chance == 0:
                print("Тебе удалось сбежать с поля боя!")
                break
            else:
                print("Монстр легко догнал тебя")
        else:
            continue

        if monsterHp > 0:
            hp -= monsterDmg
            print("Монстр атаковал и у тебя осталось", hp, "жизней.")
        
        if hp <= 0:
            break
    else:
        loot = r.randint(0, 2) + monsterLvl
        coins += loot
        print("Тебе удалось одолеть монстра, за что ты получил", loot, "монет.")
        printCoins()
    
# инициализация игры 
def initGame(initHp, initCoins, initDmg):
    global hp
    global coins
    global damage

    hp = initHp
    coins = initCoins
    damage = initDmg

    print('Ты отправился в темный, страшный лес')
    # включаем функцию
    printParameters()
    
# рандомная ситуация - число
def gameLoop():
    situation = r.randint(0, 8)
    
    if situation == 0:
        meetShop() 
    elif situation == 1:
        meetMonster()
    else:
        input('Блуждаю...')

initGame(3, 10, 1)  # передаем аргументы хп, деньги, урон

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала (да/нет): ").lower() == "да":
            initGame(3, 5, 1)
        else:
            break

    
