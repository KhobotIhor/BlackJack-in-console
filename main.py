import random

game = True

def play_mode():
    play = input("\nDo you want to play the game of Blackjack? Type 'yes' or 'no'. ")
    if play == 'yes':

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        user_cards = []
        computer_cards = []
        num = 2
        user_total_score = 0
        computer_total_score = 0

        def card_add(list1, list2, num, score1, score2):
            for i in range(0, num):
                list1.append(random.choice(cards))
                list2.append(random.choice(cards))

            for item in list1:
                score1 += item
            for item in list2:
                score2 += item

            if score1 > 21:
                print(f'\nYour cards are: {list1}, total score: {score1}')
                print(f"Computer's cards are: {list2},total score: {score2} ")
                print('\nYour score is greater than 21, so you lose)')
                play_mode()
            else:
                print(f'\nYour cards are: {list1}, total score: {score1}')
                print(f"Computer's first card is: {list2[0]}")
                num = 1
                resume = input("\nType 'add' to get another card or type 'pass' to pass. ")

                if resume == 'add':
                    card_add(user_cards, computer_cards, num, user_total_score, computer_total_score)
                else:
                    print(f'\nYour cards are: {list1}, total score: {score1}')
                    print(f"Computer's cards are: {list2},total score: {score2} ")
                    if score2 > 21:
                        print("\nComputer's score is greater than 21, so you won!!!")
                    else:
                        n1 = 21 - score1
                        n2 = 21 - score2
                        if n1 < n2:
                            print('\nCongratulations!!! You won!!!!')
                        elif n2 < n1:
                            print('\nUnfortunately, you lost)')
                        else:
                            print('\nFriendly draw!')
                        play_mode()

        card_add(user_cards, computer_cards, num, user_total_score, computer_total_score)


play_mode()
