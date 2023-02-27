game = input()
namegame = []
while:
    if game in namegame:
        print('Игра есть в списке')
    elif namegame.extend(game):
        print(namegame.sort())
    elif game == 0:
        break

games = []
game = input("Enter name of the game you wanna play: ")

while game != "0":
    if game not in games:
        games.append(game)
    else:
        print("This game is already in list.")
    game = input("Enter name of the game you wanna play: ")

print(', '.join(sorted(games)))
