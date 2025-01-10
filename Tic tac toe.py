import random
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tkboot

# Windows
window = tkboot.Window(themename='darkly')
window.title('Tic Tac Toe!')

# Game Logic + Funcs
def reset_game():
    global squares
    for button in for_draw_check:
        button.config(text="")
        button['state'] = 'normal'
    squares.clear()
    for btn in for_draw_check:
        squares.append(btn)
def win_checker():
    if x1_b['text'] == 'X' and x2_b['text'] == 'X' and x3_b['text'] == 'X' or x4_b['text'] == 'X' and x5_b['text'] == 'X' and x6_b['text'] == 'X' or x7_b['text'] == 'X' and x8_b['text'] == 'X' and x9_b['text'] == 'X' \
        or x1_b['text'] == 'X' and x4_b['text'] == 'X' and x7_b['text'] == 'X' or x2_b['text'] == 'X' and x5_b['text'] == 'X' and x8_b['text'] == 'X' or x3_b['text'] == 'X' and x6_b['text'] == 'X' and x9_b['text'] == 'X' \
        or x1_b['text'] == 'X' and x5_b['text'] == 'X' and x9_b['text'] == 'X' or x3_b['text'] == 'X' and x5_b['text'] == 'X' and x7_b['text'] == 'X':
        window1 = tkboot.Window()
        win_label = tk.Label(window1,text='You Won!',font='Consolas,10')
        win_label.grid(columnspan=2 ,padx=5,pady=5)
        play_again_button = tk.Button(window1,text='Play again!',command=lambda:(reset_game(),window1.destroy()))
        play_again_button.grid(row=1,column=0,padx=(0,20),pady=2)
        quit_button = tk.Button(window1,text='Quit',command=lambda:(window1.destroy(),window.destroy()))
        quit_button.grid(row=1,column=1,padx=(70,0),pady=2)
        for buttons in for_draw_check:
            buttons['state'] = 'disabled'

    # Loose checker
    elif x1_b['text'] == 'O' and x2_b['text'] == 'O' and x3_b['text'] == 'O' or x4_b['text'] == 'O' and x5_b['text'] == 'O' and x6_b['text'] == 'O' or x7_b['text'] == 'O' and x8_b['text'] == 'O' and x9_b['text'] == 'O' \
        or x1_b['text'] == 'O' and x4_b['text'] == 'O' and x7_b['text'] == 'O' or x2_b['text'] == 'O' and x5_b['text'] == 'O' and x8_b['text'] == 'O' or x3_b['text'] == 'O' and x6_b['text'] == 'O' and x9_b['text'] == 'O' \
        or x1_b['text'] == 'O' and x5_b['text'] == 'O' and x9_b['text'] == 'O' or x3_b['text'] == 'O' and x5_b['text'] == 'O' and x7_b['text'] == 'O':
        window1 = tkboot.Window()
        loose_label1 = tk.Label(window1,text='You Lost!',font='Consolas,10')
        loose_label1.grid(columnspan=2 ,padx=5,pady=5)
        play_again_button1 = tk.Button(window1,text='Play again!',command=lambda:(reset_game(),window1.destroy()))
        play_again_button1.grid(row=1,column=0,padx=(0,20),pady=2)
        quit_button1 = tk.Button(window1,text='Quit',command=lambda:(window1.destroy(),window.destroy()))
        quit_button1.grid(row=1,column=1,padx=(70,0),pady=2)
        for buttons in for_draw_check:
            buttons['state'] = 'disabled'

    # Draw checker
    elif all(button['text'] != "" for button in for_draw_check):
        window1 = tkboot.Window()
        draw_label1 = tk.Label(window1,text='Draw',font='Consolas,10')
        draw_label1.grid(columnspan=2 ,padx=5,pady=5)
        play_again_button2 = tk.Button(window1,text='Play again!',command=lambda:(reset_game(),window1.destroy()))
        play_again_button2.grid(row=1,column=0,padx=(0,20),pady=2)
        quit_button2 = tk.Button(window1,text='Quit',command=lambda:(window1.destroy(),window.destroy()))
        quit_button2.grid(row=1,column=1,padx=(70,0),pady=2)
        for buttons in for_draw_check:
            buttons['state'] = 'disabled'
def computer_move_func():
    global squares
    squares_copy = squares[:]

    for button in squares: # Access all the buttons
        if button['text'] == 'X' or button['text'] == 'O':
            squares.remove(button)

    if squares:
        computer_move = random.choice(squares)
        if computer_move['text'] == '':
            computer_move['text'] = 'O'
def move_checker(button):
    global squares
    if button['text'] == "":
        button.config(text='X')
        squares.remove(button)
        computer_move_func()

# Buttons
x1_b = ttk.Button(window,width=6,command=lambda:(move_checker(x1_b),win_checker()),text="")
x1_b.grid(row=0, column=0, ipady=14, padx=1, pady=1)

x2_b = ttk.Button(window, width=6, command=lambda:(move_checker(x2_b),win_checker()),text="")
x2_b.grid(row=0, column=1, ipady=14, padx=1, pady=1)

x3_b = ttk.Button(window, width=6, command=lambda:(move_checker(x3_b),win_checker()),text="")
x3_b.grid(row=0, column=2, ipady=14, padx=1, pady=1)

x4_b = ttk.Button(window, width=6, command=lambda:(move_checker(x4_b),win_checker()),text="")
x4_b.grid(row=1, column=0, ipady=14, padx=1, pady=1)

x5_b = ttk.Button(window, width=6, command=lambda:(move_checker(x5_b),win_checker()),text="")
x5_b.grid(row=1, column=1, ipady=14, padx=1, pady=1)

x6_b = ttk.Button(window, width=6, command=lambda:(move_checker(x6_b),win_checker()),text="")
x6_b.grid(row=1, column=2, ipady=14, padx=1, pady=1)

x7_b = ttk.Button(window, width=6, command=lambda:(move_checker(x7_b),win_checker()),text="")
x7_b.grid(row=2, column=0, ipady=14, padx=1, pady=1)

x8_b = ttk.Button(window, width=6, command=lambda:(move_checker(x8_b),win_checker()),text="")
x8_b.grid(row=2, column=1, ipady=14, padx=1, pady=1)

x9_b = ttk.Button(window, width=6, command=lambda:(move_checker(x9_b),win_checker()),text="")
x9_b.grid(row=2, column=2, ipady=14, padx=1, pady=1)
squares = [x1_b, x2_b, x3_b, x4_b, x5_b, x6_b, x7_b, x8_b, x9_b]
for_draw_check = [x1_b, x2_b, x3_b, x4_b, x5_b, x6_b, x7_b, x8_b, x9_b]

# Run
window.mainloop()