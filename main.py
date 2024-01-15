import time
import random
from random import choices

start_stage = 2
start_round = 0
start_level = 2
start_exp = 0
start_balance = 5
start_hp = 100

one_costs = []
two_costs = []
three_costs = []
four_costs = []
five_costs = []
one_stars = []
two_stars = []
three_stars = []


def read_txt():
    file1 = open("champions 1 cost.txt", "r")
    file2 = open("champions 2 cost.txt", "r")
    file3 = open("champions 3 cost.txt", "r")
    file4 = open("champions 4 cost.txt", "r")
    file5 = open("champions 5 cost.txt", "r")

    for line in file1:
        data = line.split(";")
        unit = data[0]
        unit_pool = int(data[2])
        for _ in range(unit_pool):
            one_costs.append(unit)

    for line in file2:
        data = line.split(";")
        unit = data[0]
        unit_pool = int(data[2])
        for _ in range(unit_pool):
            two_costs.append(unit)

    for line in file3:
        data = line.split(";")
        unit = data[0]
        unit_pool = int(data[2])
        for _ in range(unit_pool):
            three_costs.append(unit)

    for line in file4:
        data = line.split(";")
        unit = data[0]
        unit_pool = int(data[2])
        for _ in range(unit_pool):
            four_costs.append(unit)

    for line in file5:
        data = line.split(";")
        unit = data[0]
        unit_pool = int(data[2])
        for _ in range(unit_pool):
            five_costs.append(unit)

    file1.close()
    file2.close()
    file3.close()
    file4.close()
    file5.close()


def refresh_shop(level, one, two, three, four, five):
    shop = []
    match level:
        case 1:
            for _ in range(5):
                unit = random.choice(one)
                one.remove(unit)
                shop.append(unit)

        case 2:
            for _ in range(5):
                unit = random.choice(one)
                one.remove(unit)
                shop.append(unit)

        case 3:
            tier_list = [1, 2, 3, 4, 5]
            chances = [75, 25, 0, 0, 0]
            for _ in range(5):
                tier = choices(tier_list, chances).pop()
                match tier:
                    case 1:
                        unit = random.choice(one)
                        one.remove(unit)
                        shop.append(unit)
                    case 2:
                        unit = random.choice(two)
                        two.remove(unit)
                        shop.append(unit)
                    case 3:
                        unit = random.choice(three)
                        three.remove(unit)
                        shop.append(unit)
                    case 4:
                        unit = random.choice(four)
                        four.remove(unit)
                        shop.append(unit)
                    case 5:
                        unit = random.choice(five)
                        five.remove(unit)
                        shop.append(unit)

        case 4:
            tier_list = [1, 2, 3, 4, 5]
            chances = [55, 30, 15, 0, 0]
            for _ in range(5):
                tier = choices(tier_list, chances).pop()
                match tier:
                    case 1:
                        unit = random.choice(one)
                        one.remove(unit)
                        shop.append(unit)
                    case 2:
                        unit = random.choice(two)
                        two.remove(unit)
                        shop.append(unit)
                    case 3:
                        unit = random.choice(three)
                        three.remove(unit)
                        shop.append(unit)
                    case 4:
                        unit = random.choice(four)
                        four.remove(unit)
                        shop.append(unit)
                    case 5:
                        unit = random.choice(five)
                        five.remove(unit)
                        shop.append(unit)

        case 5:
            tier_list = [1, 2, 3, 4, 5]
            chances = [45, 33, 20, 2, 0]
            for _ in range(5):
                tier = choices(tier_list, chances).pop()
                match tier:
                    case 1:
                        unit = random.choice(one)
                        one.remove(unit)
                        shop.append(unit)
                    case 2:
                        unit = random.choice(two)
                        two.remove(unit)
                        shop.append(unit)
                    case 3:
                        unit = random.choice(three)
                        three.remove(unit)
                        shop.append(unit)
                    case 4:
                        unit = random.choice(four)
                        four.remove(unit)
                        shop.append(unit)
                    case 5:
                        unit = random.choice(five)
                        five.remove(unit)
                        shop.append(unit)

        case 6:
            tier_list = [1, 2, 3, 4, 5]
            chances = [25, 40, 30, 5, 0]
            for _ in range(5):
                tier = choices(tier_list, chances).pop()
                match tier:
                    case 1:
                        unit = random.choice(one)
                        one.remove(unit)
                        shop.append(unit)
                    case 2:
                        unit = random.choice(two)
                        two.remove(unit)
                        shop.append(unit)
                    case 3:
                        unit = random.choice(three)
                        three.remove(unit)
                        shop.append(unit)
                    case 4:
                        unit = random.choice(four)
                        four.remove(unit)
                        shop.append(unit)
                    case 5:
                        unit = random.choice(five)
                        five.remove(unit)
                        shop.append(unit)

        case 7:
            tier_list = [1, 2, 3, 4, 5]
            chances = [19, 30, 35, 15, 1]
            for _ in range(5):
                tier = choices(tier_list, chances).pop()
                match tier:
                    case 1:
                        unit = random.choice(one)
                        one.remove(unit)
                        shop.append(unit)
                    case 2:
                        unit = random.choice(two)
                        two.remove(unit)
                        shop.append(unit)
                    case 3:
                        unit = random.choice(three)
                        three.remove(unit)
                        shop.append(unit)
                    case 4:
                        unit = random.choice(four)
                        four.remove(unit)
                        shop.append(unit)
                    case 5:
                        unit = random.choice(five)
                        five.remove(unit)
                        shop.append(unit)

        case 8:
            tier_list = [1, 2, 3, 4, 5]
            chances = [16, 20, 35, 25, 4]
            for _ in range(5):
                tier = choices(tier_list, chances).pop()
                match tier:
                    case 1:
                        unit = random.choice(one)
                        one.remove(unit)
                        shop.append(unit)
                    case 2:
                        unit = random.choice(two)
                        two.remove(unit)
                        shop.append(unit)
                    case 3:
                        unit = random.choice(three)
                        three.remove(unit)
                        shop.append(unit)
                    case 4:
                        unit = random.choice(four)
                        four.remove(unit)
                        shop.append(unit)
                    case 5:
                        unit = random.choice(five)
                        five.remove(unit)
                        shop.append(unit)

        case 9:
            tier_list = [1, 2, 3, 4, 5]
            chances = [9, 15, 30, 30, 16]
            for _ in range(5):
                tier = choices(tier_list, chances).pop()
                match tier:
                    case 1:
                        unit = random.choice(one)
                        one.remove(unit)
                        shop.append(unit)
                    case 2:
                        unit = random.choice(two)
                        two.remove(unit)
                        shop.append(unit)
                    case 3:
                        unit = random.choice(three)
                        three.remove(unit)
                        shop.append(unit)
                    case 4:
                        unit = random.choice(four)
                        four.remove(unit)
                        shop.append(unit)
                    case 5:
                        unit = random.choice(five)
                        five.remove(unit)
                        shop.append(unit)

    return shop


def level_up(level, exp, balance):
    next_exp = 0
    match level:
        case 2:
            next_exp = 2

        case 3:
            next_exp = 6

        case 4:
            next_exp = 10

        case 5:
            next_exp = 24

        case 6:
            next_exp = 40

        case 7:
            next_exp = 60

        case 8:
            next_exp = 84

    while True:
        print(f"\nYou need {next_exp - exp} Exp to get to level {level + 1}.")
        print(f"You have {balance} gold.")
        print("How much Exp do you want to buy? (4 gold for 4 Exp)")
        choice = int(input("'0' to cancel. "))
        if choice % 4 == 0 and choice <= balance:
            if choice >= next_exp:
                level += 1
                exp = (exp + choice) - next_exp
                balance = balance - choice
                print(f"You bought {choice} Exp. You have {balance} gold left.")
                print(f"You are now level {level} with {exp} Exp.")
                time.sleep(2)
            else:
                exp = exp + choice
            break
        elif choice > balance:
            print(f"\nYou don't have enough gold to buy {choice} Exp.")
            time.sleep(2)
        elif choice == 0:
            break
        else:
            print("Please enter a number divisible with 4.")
            time.sleep(2)

    return level, exp, balance


def sell_unit(one, two, three, four, five, one_stars, two_stars, three_stars, balance):
    gold = 0
    choice = input("Which unit do you want to sell? ")
    file = open("all champions.txt", "r")
    for line in file:
        data = line.split(";")
        unit = data[0]
        unit_cost = int(data[1])
        if choice == unit:
            if unit_cost == 1:
                one.append(choice)
                gold = 1
            elif unit_cost == 2:
                two.append(choice)
                gold = 2
            elif unit_cost == 3:
                three.append(choice)
                gold = 3
            elif unit_cost == 4:
                four.append(choice)
                gold = 4
            elif unit_cost == 5:
                five.append(choice)
                gold = 5

    if choice in one_stars:
        one_stars.remove(choice)

    elif choice in two_stars:
        two_stars.remove(choice)
        gold = (gold * 3) - 1

    elif choice in three_stars:
        three_stars.remove(choice)
        gold = (gold * 9) - 1

    balance = balance + gold
    file.close()
    print(f"You have sold '{choice}' for {gold} gold.")
    return one, two, three, four, five, one_stars, two_stars, three_stars, balance


def show_options():
    print("\nYou have following options:")
    print("1. Enter unit name to buy the unit.")
    print("2. 'D' to refresh your shop.")
    print("3. 'E' to sell a unit.")
    print("4. 'F' to buy level for Exp.")
    print("5. 'X' to fight and go the next round.")


def user_manage_board(level, exp, balance, one, two, three, four, five, one_stars, two_stars, three_stars):
    shop = refresh_shop(level, one, two, three, four, five)
    while True:
        print(f"\nYou are level {level} with {exp} Exp.")
        print(f"You have {balance} gold.")
        print(f"You have {one_stars} as one stars.")
        print(f"You have {two_stars} as two stars.")
        print(f"You have {three_stars} as three stars.")
        print(f"Current shop is {shop}.")
        print("What do you want to do? ('O' to show the options).")
        choice = input().capitalize()
        file = open("all champions.txt", "r")
        if choice in shop:
            for line in file:
                data = line.split(";")
                unit = data[0]
                unit_cost = int(data[1])
                if choice == unit:
                    if balance < unit_cost:
                        print(f"You have not enough gold left. That's not enough to buy this unit: '{choice}'")
                        time.sleep(1)

                    else:
                        balance = balance - unit_cost
                        one_stars.append(choice)
                        one_stars.sort()
                        shop.remove(choice)
                        if choice in one:
                            one.remove(choice)
                        elif choice in two:
                            two.remove(choice)
                        elif choice in three:
                            three.remove(choice)
                        elif choice in four:
                            four.remove(choice)
                        elif choice in five:
                            five.remove(choice)

                        print(f"You bought '{choice}'.")
                        pairs = one_stars.count(choice)
                        if pairs == 3:
                            two_stars.append(choice)
                            for _ in range(3):
                                one_stars.remove(choice)
                            print(f"You have upgraded your '{choice}' to a 2 star.")

                        pairs2 = two_stars.count(choice)
                        if pairs2 == 3:
                            three_stars.append(choice)
                            for _ in range(3):
                                two.remove(choice)
                            print(f"You have upgraded your '{choice}' to a 3 star.")
                        time.sleep(1)

        elif choice == "X":
            for line in file:
                data = line.split(";")
                unit = data[0]
                unit_cost = data[1]
                for unused_unit in shop:
                    if unused_unit == unit:
                        if unit_cost == 1:
                            one.append(unused_unit)
                        elif unit_cost == 2:
                            two.append(unused_unit)
                        elif unit_cost == 3:
                            three.append(unused_unit)
                        elif unit_cost == 4:
                            four.append(unused_unit)
                        elif unit_cost == 5:
                            five.append(unused_unit)
            break

        elif choice == "D":
            shop = refresh_shop(level, one, two, three, four, five)
            print("You used 2 gold to refresh the shop.")
            balance -= 2

        elif choice == "E":
            one, two, three, four, five, one_stars, two_stars, three_stars, balance = sell_unit(one, two, three, four, five, one_stars, two_stars, three_stars, balance)

        elif choice == "F":
            level, exp, balance = level_up(level, exp, balance)

        elif choice == "O":
            show_options()
            time.sleep(2)

        else:
            print("Please enter a unit in the current shop.")
            time.sleep(1)

        file.close()
    return balance, level, exp, one_stars, two_stars, three_stars


def play_round(stage, one_stars, two_stars, three_stars, hp):
    enemy_value = 0
    match stage:
        case 1:
            enemy_value = 1
        case 2:
            enemy_value = random.randint(3, 7)
        case 3:
            enemy_value = random.randint(5, 10)
        case 4:
            enemy_value = random.randint(7, 12)
        case 5:
            enemy_value = random.randint(10, 14)
        case 6:
            enemy_value = random.randint(12, 18)
        case 7:
            enemy_value = random.randint(14, 20)

    your_value = len(one_stars) + (len(two_stars) * 2) + (len(three_stars) * 3)
    print(f"You have a {your_value} value board.")
    print(f"Enemy has a {enemy_value} value board.")
    if your_value >= enemy_value:
        print("You win this round.")

    elif enemy_value > your_value:
        hp = hp - (enemy_value - your_value)
        print(f"You lost this round. You lost {enemy_value - your_value} HP.")
        print(f"You have {hp} HP left.")
        time.sleep(2)

    return hp


def main(stage, tft_round, level, exp, balance, one_stars, two_stars, three_stars):
    while True:
        if stage == 8:
            print("\nGame over.")
            exit()

        balance += 5
        tft_round += 1
        exp += 2

        if level == 2 and exp == 2:
            exp = 0
            level += 1

        elif level == 3 and exp == 6:
            exp = 0
            level += 1

        elif level == 4 and exp == 10:
            exp = 0
            level += 1

        elif level == 5 and exp == 24:
            exp = 0
            level += 1

        elif level == 6 and exp == 40:
            exp = 0
            level += 1

        elif level == 7 and exp == 40:
            exp = 0
            level += 1

        elif level == 8 and exp == 64:
            exp = 0
            level += 1

        show_options()
        print(f"\nCURRENT STAGE IS {stage}. CURRENT ROUND IS {tft_round}.")
        balance, level, exp, one_stars, two_stars, three_stars = user_manage_board(level, exp, balance, one_costs, two_costs, three_costs, four_costs, five_costs, one_stars, two_stars, three_stars)
        hp = play_round(stage, one_stars, two_stars, three_stars, start_hp)
        time.sleep(2)
        if hp <= 0:
            print("\nYou lost the game.")
            exit()

        if tft_round == 6:
            tft_round = 0
            stage += 1

        main(stage, tft_round, level, exp, balance, one_stars, two_stars, three_stars)


read_txt()
main(start_stage, start_round, start_level, start_exp, start_balance, one_stars, two_stars, three_stars)
