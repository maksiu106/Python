#!/usr/bin/env python3
#coding=utf-8

import tkinter as tk
import random

global n1, n2

#0 - kamień, 1 - papier, 2 - nożyce
def game(x):
	global n1, n2
	computer = random.randint(0, 2)
	if (computer == 0): opponent = "Kamień"
	elif (computer == 1): opponent = "Papier"
	else: opponent = "Nożyce"
	
	if (x == computer):
		message = "Nastąpił remis. Spróbuj jeszcze raz, może się uda."
	elif (x == 0 and computer == 2) or (x == 1 and computer == 0) or (x == 2 and computer == 1):
		message = "Wygrałeś z komputerem! Super!"
		n1 += 1
	else:
		message = "Tym razem się nie udało... przegrałeś ze swoim komputerem."
		n2 += 1
	
	message = "Wybór komputera: " + opponent + "\n\n" + message
	result.config(text=message)
	score = "Wynik\n\n\tTy    " + str(n1) + " - " + str(n2) + "    Komputer   "
	score_label.config(text=score)

window = tk.Tk()
window.title("Rock, scissors, stone")
window.geometry("500x450")

name = tk.Label(window, text="Gra w kamień, papier, nożyce")
font="Times 20 bold"
name.pack(pady=20)

n1 = 0
n2 = 0

zero_button = tk.Button(window, text="Wybierz kamień", command=lambda: game(0))
zero_button.pack(pady=5)

one_button = tk.Button(window, text="Wybierz papier", command=lambda: game(1))
one_button.pack(pady=5)

two_button = tk.Button(window, text="Wybierz nożyce", command=lambda: game(2))
two_button.pack(pady=5)

quit_button = tk.Button(window, text="Wyjdź z gry", command = window.quit)
quit_button.pack(pady = 15)

result = tk.Label(window, text="")
result.pack(pady=20)

score_label = tk.Label(window, text="")
score_label.pack(pady=1)

window.mainloop()

