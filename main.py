import os
import platform

board = list(range(1,10))

print(str(platform.system()))

def out_red(text):
    return "\033[31m {}".format(text)

def out_yellow(text):
    return "\033[33m {}".format(text)

def out_blue(text):
    return "\033[34m {}".format(text)

def out_oth(text):
    return "\033[35m {}".format(text)

def cls():
    if str(platform.system()) == "Windows" :
        os.system('CLS')
    else:
        os.system('clear')
def out_tocken(t):
    if t == "X" :
         return out_red(t)
    elif t == "O" :
         return out_blue(t)
    else :
        return out_yellow(t)

def draw_board(board):
    print(out_yellow("-------------------"))
    for i in range(3):
        print(out_yellow("|"), out_tocken(board[0+i*3]), out_yellow("|"), out_tocken(board[1+i*3]), out_yellow("|"), out_tocken(board[2+i*3]), out_yellow("|"))
        print(out_yellow("-------------------"))

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        cls()
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                cls()
                draw_board(board)
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            cls()
            draw_board(board)
            print ("Ничья!")
            break
    x = input('Нажмите любую клавишу')

main(board)

