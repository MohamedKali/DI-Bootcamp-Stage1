from os import system
from time import sleep
import random
def gestion_erreur(message):
    while True:
        try:
            x=int(input(message))
            return x
       
        except ValueError:
            print("\nErreur de saisir ❌❌\n")

def input_player(player,p1,p2):
    row=gestion_erreur(f"\nEntrer la ligne {player}: ")
    while row<=0 or row>=4:
        print("Ligne inexistante ❌❌\n")
        row=gestion_erreur(f"Entrer la ligne {player}: ")

    col=gestion_erreur(f"Entrer la colonne {player}: ")
    print("\n")
    while col<=0 or col>=4:
        print("Ligne inexistante ❌❌\n")
        col=gestion_erreur(f"Entrer la ligne {player}: ")

    a=(row-1,col-1)
    if a in p1 or a in p2:
        return
    else:
        return a


def begin(p1,p2):
    
    if random.choice(['X','O'])=='X':
        c,b='X','O'
    else:
        c,b='O','X'
    while True:
        a=input_player(c,p1,p2)
        while a == None:
            print("\ncase occupee ❌❌")
            #system("pause")
            sleep(1)
            system("cls")
            display_board(p1,p2,c)
            a=input_player(c,p1,p2)
        if c == 'X':
            p1.append(a)
        else:
            p2.append(a)
        vic=display_board(p1,p2,c)
        vic=victoire(vic)

        if vic == True:
            print(f"\nbravo joueur {c} vous avez gagner la partie!!!\n")
            break
        elif vic == False :
            print(f"\nMacth Null !!!\n")
            break
        a=input_player(b,p1,p2)
        while a == None:
            print("\ncase occupee ❌❌")
            #system("pause")
            sleep(0.6)
            system("cls")
            display_board(p1,p2,b)
            a=input_player(b,p1,p2)
        if b== 'O':
            p2.append(a)
        else:
            p1.append(a)
        vic=display_board(p1,p2,b)
        vic=victoire(vic)

        if vic == True:
            print(f"\nbravo joueur {b} vous avez gagner la partie!!!\n")
            break
        elif vic == False :
            print(f"\nMacth Null !!!\n")
            break

def victoire(x):
    if (x[0][0],x[1][1],x[2][2]) ==('X','X','X') or (x[0][0],x[1][1],x[2][2]) ==('O','O','O'):
        return True
    elif (x[0][0],x[0][1],x[0][2]) ==('X','X','X') or (x[0][0],x[0][1],x[0][2]) ==('O','O','O'):
        return True
    elif (x[1][0],x[1][1],x[1][2]) ==('X','X','X') or (x[1][0],x[1][1],x[1][2]) ==('O','O','O'):
        return True
    elif (x[2][0],x[2][1],x[2][2]) ==('X','X','X') or (x[2][0],x[2][1],x[2][2]) ==('O','O','O'):
        return True
    elif (x[0][0],x[1][0],x[2][0]) ==('X','X','X') or (x[0][0],x[1][0],x[2][0]) ==('O','O','O'):
        return True
    elif (x[0][1],x[1][1],x[2][1]) ==('X','X','X') or (x[0][1],x[1][1],x[2][1]) ==('O','O','O'):
        return True
    elif (x[0][2],x[1][2],x[2][2]) ==('X','X','X') or (x[0][2],x[1][2],x[2][2]) ==('O','O','O'):
        return True
    elif (x[2][0],x[1][1],x[0][2]) ==('X','X','X') or (x[2][0],x[1][1],x[0][2]) ==('O','O','O'):
        return True
    elif ' ' not in (x[0][0],x[0][1],x[0][2],x[1][0],x[1][1],x[1][2],x[2][0],x[2][1],x[2][2]):
        return False

def main():
    p1,p2=[],[]
    display_board(p1,p2,'')
    begin(p1,p2)
    

def display_board(p1,p2,c):
    x=[ [' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in p1:
        x[i[0]][i[1]]='X'

    for i in p2:
         x[i[0]][i[1]]='O'

    print("\nTIC TAC TOE")
    print("*********************")
    print(f"*  {x[0][0]}   |  {x[0][1]}  |  {x[0][2]}   *")
    print(f"* ----- ----- ----- *")
    print(f"*  {x[1][0]}   |  {x[1][1]}  |  {x[1][2]}   *")
    print(f"* ----- ----- ----- *")
    print(f"*  {x[2][0]}   |  {x[2][1]}  |  {x[2][2]}   *")
    print("*********************")
    return x

main()

