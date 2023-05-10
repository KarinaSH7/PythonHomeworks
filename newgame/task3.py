class Student:
    def __init__(self, name, sr_ball):
        self.name = name
        self.sr_ball = sr_ball
        self.cource = '-'

    def set_cource(self, new_cource):
        self.cource = new_cource
        print(self.name, 'установлен курс', self.cource)

    def print_if(self):
        if self.sr_ball < 50:
            print(self.name, 'на гране отчисления')
        else:
            print(self.name, 'в порядке')

Kaplan = Student('Каплан', 20)
# Kaplan.cource = 1
Kaplan.set_cource(1)
# print(Kaplan.cource)


Areg = Student('Аренг', 100)
Areg.set_cource(2)

Kaplan.print_if()
Areg.print_if()
