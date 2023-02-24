weight, height = [int(s) for s in input('введите вес в килограммах и рост в сантиметрах:').split()]
print(round(weight / ((height / 100) ** 2), 2))
