#!/usr/bin/env python3
#coding=utf-8

import pygame
import sys
from pygame.locals import *

pygame.init()
font = pygame.font.Font(None, 50)

#wymiary okna gry
window_width = 1200
window_height = 800

#tworzenie okienka gry
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")

#kolory
black = (0, 0, 0)
white = (255, 255, 255)

#wymiar paletek
paddle_width = 20
paddle_height = 100

#tworzenie paletek i piłki
player1 = pygame.Rect(80, window_height//2, paddle_width, paddle_height)
player2 = pygame.Rect(window_width-80-paddle_width, window_height//2, paddle_width, paddle_height)
ball = pygame.Rect(window_width//2, window_height//2, 30, 30)

#szybkość piłki
ball_speed_x = 5
ball_speed_y = 5

#wyniki
score1 = 0
score2 = 0

game_over = False
winner = "Nikt nie"

def sign(x):
	if x>0: return 1
	elif x<0: return -1
	else: return 0
	
#zapytanie o tryb gry
window.fill(black)
text = font.render(f"Tryb gry: 1 - jednoosobowy 2 - dwuosobowy", True, white)
text_rect = text.get_rect(center=(window_width//2, window_height//2))
window.blit(text, text_rect)
pygame.display.update()

mode = 0
while (mode == 0):
	for event in pygame.event.get():
		if event.type == KEYDOWN and event.key == pygame.K_1:
			mode = 1
		elif event.type == KEYDOWN and event.key == pygame.K_2:
			mode = 2

while not game_over:
	clock = pygame.time.Clock()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN and event.key == pygame.K_q:
			game_over = True
			
	#ruszanie paletkami
	keys = pygame.key.get_pressed()	
	if (keys[K_UP] and player1.y > 0):
		player1.y -= 5
	if (keys[K_DOWN] and player1.y < window_height-paddle_height):
		player1.y += 5
		
	#ruch piłeczki
	ball.x += ball_speed_x
	ball.y += ball_speed_y
	
	#dla trybu dwuosobowego
	if (mode == 2):
		if (keys[K_w] and player2.y > 0):
			player2.y -= 5
		if (keys[K_s] and player2.y < window_height-paddle_height):
			player2.y += 5
			
	#dla trybu jednoosobowego
	if mode == 1:
		if (ball_speed_x>0): #jeśli porusza się w kierunku komputera
			if (player2.y > 0 and player2.y < window_height-paddle_height): #jeśli jest w okienku
				if (ball_speed_y>0):
					player2.y += 5*sign(ball_speed_y)
				elif (ball_speed_y<0):
					player2.y += 5*sign(ball_speed_y)
			else:
				if player2.y <= 0:
					player2.y = 1
				elif player2.y >= window_height - paddle_height:
					player2.y = window_height - paddle_height - 1
			
	#gdy następuje zderzenie
	if ball.colliderect(player1):
		ball_speed_x *= -1
		ball_speed_x += 0.2
		if (ball_speed_y > 0): ball_speed_y += 0.2
		else: ball_speed_y -= 0.2
		
	if ball.colliderect(player2):
		ball_speed_x *= -1
		ball_speed_x -= 0.2
		if (ball_speed_y > 0): ball_speed_y += 0.2
		else: ball_speed_y -= 0.2
	
	if (ball.y <= 0 or ball.y+30 >= window_height):
		ball_speed_y *= -1
	
	#gdy ktoś zdobywa punkt
	if (ball.x <= 0):
		score2 += 1
		ball.x = window_width//2
		ball.y = window_height//2
		ball_speed_x = 5
		ball_speed_y = 5
		if (mode == 1):
			player2.y = window_height//2
	if (ball.x >= window_width):
		score1 += 1
		ball.x = window_width//2
		ball.y = window_height//2
		ball_speed_x = 5
		ball_speed_y = 5
		if (mode == 1):
			player2.y = window_height//2
	
	#koniec gry
	if (score1 == 11):
		winner = "Gracz 1"
		game_over = True
	elif (score2 == 11):
		winner = "Gracz 2"
		game_over = True
		
	#gra
	window.fill(black)
	pygame.draw.rect(window, white, player1)
	pygame.draw.rect(window, white, player2)
	pygame.draw.circle(window, white, ball.center, ball.width//2)
	
	#wyświetlanie wyniku
	text = font.render(f"Gracz 1: {score1}  Gracz 2: {score2}", True, white)
	window.blit(text, (10, 10))
	
	pygame.display.update()
	clock.tick(60)

#wyświetlenie informacji o zwycięzcy
window.fill(black)
text = font.render(f"{winner} wygrał!", True, white)
text_rect = text.get_rect(center=(window_width//2, window_height//2))
window.blit(text, text_rect)
pygame.display.update()

wait = True
while wait:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			wait = False
