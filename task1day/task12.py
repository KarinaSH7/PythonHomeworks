import math
a = float(input())
b = float(input())
expenditure = float(input())
litersbottels = float(input())
percent = int(input())

square = a * b
print(round(a * b, 2))

liters = square / expenditure
unused = liters * percent / 100
liters += unused

print(round(liters,2))

bottles = int(math. ceil(liters / litersbottels))
print(bottles)
print(round((float(bottles) * litersbottels) - liters,2))