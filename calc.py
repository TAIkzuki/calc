import tkinter


class Calculations:
    global a
    global b
    def __new__(cls, *args, **kwargs):
        print()
    def plus(self):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            print("in '0' not delete")
        else:
            return a / b

    def procent(self, a, b):
        return (a / b) * 100

    def root(self, a, b):
        pass

Calculations.a= int(input('a'))
Calculations.b=int(input('b'))
print(Calculations.division(se,Calculations.a,Calculations.b))
