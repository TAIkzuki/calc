import tkinter


class Calculations:
    global a
    global b

    def __init__(self):
        pass

    def plus(self, x, y):
        return x + y

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

    def mat_string(self, mat_string :str ):
        return eval(mat_string)

    def my_eval(self, my_expression):
        operators = {'+': (1, lambda x, y: x + y),
                     '-': (1, lambda x, y: x - y),
                     '*': (2, lambda x, y: x * y),
                     '/': (2, lambda x, y: x / y),
                     '**': (3, lambda x, y: x ** y)}

        def precedence(op):
            return operators[op][0] if op in operators else 0

        def evaluate(my_expression):
            operands = []
            operators = []
            num = ''
            i = 0
            while i < len(my_expression):
                char = my_expression[i]
                if char.isdigit():
                    num += char
                elif char == '(':
                    if num:
                        operands.append(int(num))
                        num = ''
                    j = i
                    nested_brackets = 1
                    while nested_brackets != 0:
                        j += 1
                        if my_expression[j] == '(':
                            nested_brackets += 1
                        elif my_expression[j] == ')':
                            nested_brackets -= 1
                    operands.append(evaluate(my_expression[i + 1:j]))
                    i = j
                else:
                    if num:
                        operands.append(int(num))
                        num = ''
                    if char in operators:
                        while operators and precedence(operators[-1]) >= precedence(char):
                            op = operators.pop()
                            right = operands.pop()
                            left = operands.pop()
                            result = operators[op][1](left, right)
                            operands.append(result)
                        operators.append(char)
                    else:
                        operators.append(char)
                i += 1

            if num:
                operands.append(int(num))

            while operators:
                op = operators.pop()
                right = operands.pop()
                left = operands.pop()
                result = operators[op][1](left, right)
                operands.append(result)

            return operands[0] if operands else None

        return evaluate(my_expression)


calc= Calculations()
stis = '12**2+18*(3+7*4)'
result= eval(stis)

result= calc.mat_string(stis)


result=calc.my_eval(stis)
print(result)