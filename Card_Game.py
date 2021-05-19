def menu(msg):
    print('-' * 35)
    print(f'\033[1m{msg:^35}\033[m')
    print('-' * 35)


def deal(list1, list2, deck):
    from random import randint
    # Limit of cards based on their suits
    flag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 0
    # Giving the cards to each player.
    for c in range(1, deck + 1):
        if turn == 0:
            while True:
                card = randint(1, 13)
                if flag[card-1] <= 4:
                    list1.append(card)
                    flag[card-1] += 1
                    break
                else:
                    continue
            turn += 1
        else:
            while True:
                card = randint(1, 13)
                if flag[card-1] <= 4:
                    list2.append(card)
                    flag[card-1] += 1
                    break
                else:
                    continue
            turn -= 1


def rounds(list1, list2):
    # Showing the results of which round
    from time import sleep
    cont = 1
    while True:
        # condition to make the game possible
        if len(list1) > 0 and len(list2) > 0:
            menu(f"ROUND {cont}")
            print(f'\033[34m{"Player 1:":<10}\033[m{list1[-1]:<5}  x  {list2[-1]:>5}\033[31m{":Player 2":>10}\033[m')
            # Round conditions
            if list1[-1] > list2[-1]:
                # if player 1 win
                list1.insert(0, list1[-1])
                list1.pop()
                list1.insert(0, list2[-1])
                list2.pop()
                print(f'\033[1m{">>PLAYER 1 WON<<":^34}\033[m')
            elif list1[-1] < list2[-1]:
                # if player 2 win
                list2.insert(0, list2[-1])
                list2.pop()
                list2.insert(0, list1[-1])
                list1.pop()
                print(f'\033[1m{">>PLAYER 2 WON<<":^34}\033[m')
            else:
                # if none win
                list1.insert(0, list1[-1])
                list1.pop()
                list2.insert(0, list2[-1])
                list2.pop()
                print(f'\033[1m{">>DRAWN<<":^35}\033[m')
            print('-' * 35)
            sleep(2)
            cont += 1
        # Someone lost all his cards
        else:
            break


# Main program
print('Assuming that the side-deck must have an even number of cards...')

menu("SIDE-DECK")

while True:
    # Making sure that the game is playable.
    try:
        deck = int(input('How many cards does this side-deck have?(Max 52.) '))
        if deck > 52:
            print('\033[31m[ERRO]\033[m Please type an number under or equal to 52.')
            continue
        elif deck % 2 == 0 and deck <= 52:
            break
        elif deck % 2 == 1:
            print('\033[31m[ERRO]\033[m Please type an even number.')
            continue
    except (ValueError, TypeError):
        print('\033[31m[ERRO] Invalid data.\033[m Please type an valid number.')
        continue

# Creating the players
player1 = []
player2 = []

deal(player1, player2, deck)

rounds(player1, player2)

# Showing the final results
if len(player1) == 0:
    print(f'\033[1;93m{"<< PLAYER 2 HAS WON! >>":^35}\033[m')
else:
    print(f'\033[1;93m{"<< PLAYER 1 HAS WON! >>":^35}\033[m')
