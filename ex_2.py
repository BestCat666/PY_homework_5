#2.Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random
all_sweet = 151
take_sweet = 0
player1_sweet = 0
player2_sweet = 0

def player1():
    global all_sweet
    global take_sweet
    global player1_sweet
    take_sweet = int(input('№1!Твой ход! Сколько конфет ты хочешь взять?: '))
    while take_sweet > 28 or take_sweet > all_sweet:
        take_sweet = int(input('Ты можешь взять не более 28 конфет за ход!Сколько конфет ты хочешь взять?: '))
    all_sweet = all_sweet - take_sweet
    player1_sweet = player1_sweet + take_sweet
    print(f'осталось {all_sweet} конфет')
    if all_sweet > 0:
        player2()    
    else:
        print(f'игрок №1 победил!')
        exit()
 

def player2():
    global all_sweet
    global take_sweet
    global player2_sweet
    take_sweet = all_sweet % 29 if all_sweet % 29 != 0 else random.randint(1, 28)
    #take_sweet = int(input('№2!Твой ход! Сколько конфет ты хочешь взять?: '))
    #while take_sweet > 28 or take_sweet > all_sweet:
        #take_sweet = int(input('Ты можешь взять не более 28 конфет за ход!Сколько конфет ты хочешь взять?: '))
    print(f'бот взял {take_sweet} конфет')
    all_sweet = all_sweet - take_sweet
    player2_sweet = player2_sweet + take_sweet
    print(f'осталось {all_sweet} конфет')
    if all_sweet > 0:
        player1()
    else:
        print(f'игрок №2/бот победил!')
        exit()

def who_first():
    rand_num = random.randint(1, 2)
    if rand_num == 1:
        print('Первым ходит игрок №1:')
        player1()
    else:
        print('Первым ходит игрок №2(или бот):')
        player2()
who_first()     
player1()
player2()





#take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else random.randint(1, 28)