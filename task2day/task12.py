import re

# string = input()
# num = re.findall(r'\d+', string)[0]
# print(num)

# print((string)(''.join(i for i in string if i.isdigit())))
s = input()
s1 = "".join(c for c in s if c.isdecimal())
s = int(s1)
print(s + 1)
