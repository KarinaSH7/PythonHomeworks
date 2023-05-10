class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    def print_info(self):
        print('дан прямоульник с длинной', self.lenght, 'и шириной', self.width)

    def ret_p(self):
        return (self.lenght+self.width) * 2

    def ret_s(self):
        return self.lenght * self.width
    def check(self, other):
        if self.lenght < other.lenght and self.width < other.width:
            print('может поместиться 1 во 2')
        else:
            print('не может')



rest1 = Rectangle(5, 10)
rest2 = Rectangle(3, 8)
rest1.print_info()
rest2.print_info()
print(rest1.ret_s())
print(rest2.ret_s())
print(rest1.ret_p())
print(rest2.ret_p())
rest2.check(rest1)
rest1.check(rest2)