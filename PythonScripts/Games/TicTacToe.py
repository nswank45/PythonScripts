from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Tic-Tac-Toe Game!')

# X Starts so true
clicked = True
count = 0

# Initializing empty board
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]]

value_dict = {
    "X": 1,
    "tie": 0,
    "O": -1
}


def winner2(board):
    # Description - determines the winner of the current board or if it is Still not  clear who will win
    # Arguments :-
    # board - a nested list which is the current snapshot of the board
    # Returns :-
    # "X" - if X wins
    # "O" - if O wins
    # "tie" - if game is a tie
    # "continue" - if the game has still not ended
    # horizontal win
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == "X":
                return "X"
            if board[i][0] == "O":
                return "O"
# vertical win
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == "X":
                return "X"
            if board[0][i] == "O":
                return "O"
# diagonal win 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return "X"
        if board[0][0] == "O":
            return "O"
# diagonal win 2
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[2][0] == "X":
            return "X"
        if board[2][0] == "O":
            return "O"
# continue
    for row in board:
        for cell in row:
            if cell == "-":
                return "continue"
# tie
    return "tie"


def minimax(board, is_this_AIs_turn):
    # Description - Implementation of the minimax algorithm
    # Arguments :-
    # board - a nested list which is the current snapshot of the board
    # is_this_AIs_turn - a boolean which is true if AI is the current Player
    # Returns :-
    # the value of the current node
    winner_player = winner2(board)
    # if we reached the end of the tree
    if winner_player != "continue":
        return value_dict[winner_player]
    # if this is AIs turn i.e the maximizing players turn
    if is_this_AIs_turn:
        score = - 2  # anything smaller than min score
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "-":
                    board[i][j] = "X"
                    curr_score = minimax(board, False)
                    board[i][j] = "-"
                    score = max(score, curr_score)
        return score
    else:
        score = 2  # anything bigger than max score
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "-":
                    board[i][j] = "O"
                    curr_score = minimax(board, True)
                    board[i][j] = "-"
                    score = min(score, curr_score)
        return score
def ais_move(board):
    # Description - determines the next move of the AI
    # Arguments :-
    # board - a nested list which is the current snapshot of the board
    # Returns :-
    # an array with 2 items representing the coordinates of the cell
    score = - 2  # anything smaller than min score
    x = -1  # the row no. of cell which AI chosses for best move
    y = -1  # the column no. of cell which AI chosses for best move
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "-":
                board[i][j] = "X"
                curr_score = minimax(board, False)
                board[i][j] = "-"
                if curr_score > score:
                    score = curr_score
                    x = i
                    y = j
    return [x, y]
# Disable all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
# Check to see if someone had won
def checkifwon():
    global winner
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
        ### CHECK FOR O WIN ###
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Pogchamp")
        disable_all_buttons()
    # Check if tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", " A tie? Really? Get better come on.")
# Button clicked functions
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        info = b.grid_info()
        x, y = info["row"], info["column"]
        board[x][y] = "O"
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
        if not winner and count < 9:
            AIs_turn = ais_move(board)
            x = AIs_turn[0]
            y = AIs_turn[1]
            board[x][y] = "X"
            button_map[x][y]["text"] = "O"
            clicked = True
            count += 1
            checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been taken Dingbat. Pay attention.")


# S Start the game over
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    global button_map
    global board
    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]
    clicked = True
    count = 0

    # Button Building
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Gray", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Gray", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Gray", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Gray", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Gray", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Gray", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Gray", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Gray", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Gray", command=lambda: b_click(b9))

    # Grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    button_map = [[b1, b2, b3],
                  [b4, b5, b6],
                  [b7, b8, b9]]


# Create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()
root.mainloop()