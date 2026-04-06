
print("tic-tac-toe game")
print("this is the postition format below.")
print(f"1|2|3\n—+—+—\n4|5|6\n—+—+—\n7|8|9")

board={1:" ",2:" ",3:" "
        ,4:" ",5:" ",6:" "
        ,7:" ",8:" ",9:" "}
team=str(input("will you be X or O?(has to be uppercase): "))
turn=0
while True:
    
    choice=int(input("enter your postition, X: "))
    print("1|2|3")
    print("—+—+—")
    print("4|5|6")
    print("—+—+—")
    print("7|8|9")
    turn+=1
    if board[choice] != " ":
            print("spot already taken, choose another")
    elif choice in board:
        board[choice] = team
        print(f"{board[1]}|{board[2]}|{board[3]}")
        print("—+—+—")
        print(f"{board[4]}|{board[5]}|{board[6]}")
        print("—+—+—")
        print(f"{board[7]}|{board[8]}|{board[9]}")
    if turn>=5:
        if board[1]==board[2]==board[3]!=" ":
            print("win")
            break
        elif board[4]==board[5]==board[6]!=" ":
            print("win")
            break 
        elif board[7]==board[8]==board[9]!=" ":
            print("win")
            break 
        elif board[1]==board[4]==board[7]!=" ":
            print("win")
            break
        elif board[2]==board[5]==board[8]!=" ":
            print("win")
            break
        elif board[3]==board[6]==board[9]!=" ":
            print("win")
            break
        elif board[1]==board[5]==board[9]!=" ":
            print("win")
            break
        elif board[3]==board[5]==board[7]!=" ":
            print("win")
            break
    if team=="X":
        team="O"
    else:
        team="X"   