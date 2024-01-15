# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:44:56 2023

@author: Dalia Salih, Julia Moor, Anton Rabanus

"""


class Board:
    
    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k
        pass
    
    def has_won():
        pass
    
    def display():
        pass
    
class Player:
    
    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number
        
    def make_move(self, board):
        pass
    
class Game:
    
    def __init__(self, m, n, k, board, player1, player2):
        self.m = m
        self.n = n
        self.k = k
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def start():
        pass
    
    def game_loop(): #eigentliches gameplay
        pass
    
    
class MyBot(Player):
    
    def __init__(self):
        pass
        
    def make_move(self, board): #überarbeiten im vergleich zu player
        pass
    
    

    
