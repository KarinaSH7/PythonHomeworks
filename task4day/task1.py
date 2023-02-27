games = []
game = input()

while game != "0":
    if game not in games:
        games.append(game)
    else:
        print("This game is already in list.")
    game = input()

print(', '.join(sorted(games)))
