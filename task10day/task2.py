"""
В каждом заплыве участвуют два случайных спортсмена из разных сборных. Напиши программу для печати номеров спортсменов.
1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением: «Число участников сборной _:».
2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате: «Пловец _ - пловец _».
"""
from random import randint as rand

team1 = int(input("Число участников сборной 1: "))
team2 = int(input("Число участников сборной 2: "))
rand_team1 = rand(1, team1)
rand_team2 = rand(1, team2)

print("Пловец", rand_team1, "- пловец", rand_team2)
