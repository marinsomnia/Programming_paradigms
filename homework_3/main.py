print()
print("*" * 10, "Крестики-нолики", "*" * 10)

# Игровое поле от 1 до 9
board = list(range(1, 10))

# Отрисовываем начальное игровое поле
def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|",  board[1 + i * 3], "|",  board[2 + i * 3], "|")
        print("-" * 13)

# Функция хода игрока
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input(f'Куда поставим: {player_token} ? ')
        # Обработка исключения, если введено не число
        try:
            player_answer = int(player_answer)
        except:
            print("Некоректный ввод. Введите число еще раз.")
            continue
        if player_answer >= 1 and player_answer <= 9:
            # Проверка занята ли клетка на поле или нет
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Введите число от 1 до 9")

# Функция проверки победителя
def check_win(board):
    # Выигрышные позиции на поле
    win_position = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    # Проверка на выигрышные позиции
    for each in win_position:
        if board[each[0]] ==  board[each[1]] ==  board[each[2]]:
            return  board[each[0]]
    return False

# Начало игры
def start_game(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        # Выбор игрока: X или O
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(f'Выиграл игрок {tmp}')
                win = True
        if counter == 9:
            print("Ничья!")
            win = True
    draw_board(board)

start_game(board)

'''
Это структурная парадигма, так как это императивный стиль, который основан на последовательном исполнении хорошо
структурированных “блоков” (утверждение,ветвление, цикл) без goto. 
Это так же и процедурная парадигма, так как это последовательность команд, выделенная в отдельные блоки кода,
которые можно вызывать по их имени, то есть имени процедуры. 
'''