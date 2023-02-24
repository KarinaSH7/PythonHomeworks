# number = input().split(" ")
# for i in number:
# if i.find("@") != -1:
# print(i)


text = input(" ").split("@")
last = text[0].split()[-1]
first = text[1].split()[0]
print(last + "@" + first)
