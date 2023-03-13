people = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
people['Scaf'] = 34
total = sum(people[x] for x in people)

print(total)