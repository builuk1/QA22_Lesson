# a = 0
# while a < 10 and a != 5:
#     print(a)
#     a = a + 1
#
# for i in range(10):
#     if i == 5:
#         break#сломает цикл, в момент вызова, любой цикл while или for
#     print(i)
#
# for i in range(10):
#     if i == 5:
#         continue #всё что ниже него в данном цикле будет пропущенно, любой цикл while или for
#     print(i)
#
# #Дано рандомное число. Пользователь вводит любое число от 1 до 10. Это число отнимается от загадонного
# #Задача, получить в итоге 0.
#
# import random
# number = random.randint(90,150)
# print(number)
# while number != 0:
#     while True:
#         my_number = int(input("Enter number [1-9]: "))
#         if my_number >= 1 and my_number <= 9:
#             break
#     if (number - my_number) < 0:
#         continue
#     number = number - my_number
# #    print(number)#Режим отладки, по задумке число не должно быть видно, заставляем пользователя учить математику
# print('You win!')

# Rock Paper Scissors /// Камень Ножницы Бумага
# Объявление переменных
# import random
#
# player_score = 0
# bot_score = 0
# player_choice = ''
# bot_choice = ''
# # i = 0#только для while
# # while player_score <= 3 and bot_score <= 3:
# for i in range(1, 4):
#     # i = i + 1#только для while
#     print(f'ROUND {i}')
#     # Ход игрока 1
#     player_choice = ''
#     while player_choice != 'r' and player_choice != 'p' and player_choice != 's':
#         player_choice = str(input("Enter [r],[p],[s] : "))  # l - Lizard, k -Spock
#     # Ход игрока 2 / бота
#     bot_choice = random.choice('rps')
#     # Обратная связь
#     print(f'Player choice : {player_choice} Bot choice : {bot_choice}')
#     if player_choice == bot_choice:
#         print('Draw round')
#     elif player_choice == 'r':
#         if bot_choice == 's':
#             print('Player won the round!')
#             player_score = player_score + 1
#         else:
#             print('Bot won the round!')
#             bot_score = bot_score + 1
#     elif player_choice == 's':
#         if bot_choice == 'p':
#             print('Player won the round!')
#             player_score = player_score + 1
#         else:
#             print('Bot won the round!')
#             bot_score = bot_score + 1
#     elif player_choice == 'p':
#         if bot_choice == 'r':
#             print('Player won the round!')
#             player_score = player_score + 1
#         else:
#             print('Bot won the round!')
#             bot_score = bot_score + 1
# if player_score == bot_score:
#     print('Draw game')
# elif player_score > bot_score:
#     print('Player won game!')
# elif player_score < bot_score:
#     print('Bot won game!')
#

for i in 0.1, 0.2, 0.3:
    print(i)

a = 0.0
while a < 10.0:
    print(a)
    a = a + 0.1
