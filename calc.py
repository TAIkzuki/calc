class DemoExprEvaluator:
    class CalcResult:
        def __init__(self, operation_occurred, result_string):
            self.operation_occurred = operation_occurred
            self.result_string = result_string

    def __init__(self):
        pass

    def spread_space_between_tokens(self, inbox_str):
        arr = []
        for c in inbox_str:
            if c in '()*/^+-':
                arr.append(' ' + c + ' ')
            elif c.isdigit():
                arr.append(c)
        return ''.join(arr).strip()

    def get_lexems(self, expr):
        expr = self.spread_space_between_tokens(expr)
        lexems = expr.split()
        return lexems

    def apply_operator(self, expr_without_parens, operator):
        '''func apply operator on priority'''
        stack = []
        lexems = self.get_lexems(expr_without_parens)
        for lexem in lexems:
            stack.append(lexem)
            if len(stack) >= 3:
                left, middle, right = stack[-3:]
                if middle == operator:
                    operand1 = int(left)
                    operand2 = int(right)
                    res = 0
                    if operator == '^':
                        res = operand1 ** operand2
                    elif operator == '*':
                        res = operand1 * operand2
                    elif operator == '/':
                        res = operand1 / operand2
                    elif operator == '+':
                        res = operand1 + operand2
                    elif operator == '-':
                        res = operand1 - operand2
                    stack = stack[:-3]
                    stack.append(str(res))
        return ''.join(stack)

    def eval_expr_without_parens(self, expr_without_parens):
        result = self.apply_operator(expr_without_parens, "^")
        result = self.apply_operator(result, "*")
        result = self.apply_operator(result, "/")
        result = self.apply_operator(result, "+")
        result = self.apply_operator(result, "-")
        return result

    def open_single_paren(self, expr):
        ''' '''
        r = self.CalcResult(False, expr)
        lexems = self.get_lexems(expr)
        stack = []
        lp_index = 0
        for i, lexem in enumerate(lexems):
            stack.append(lexem)
            if lexem == "(":
                lp_index = i
            if lexem == ")" and not r.operation_occurred:
                stack.pop()
                num_of_items_to_pop = i - lp_index - 1
                ewp = []
                for j in range(num_of_items_to_pop):
                    ewp.insert(0, stack.pop())
                ewp_eval_result = self.eval_expr_without_parens(''.join(ewp))
                stack.pop()
                stack.append(ewp_eval_result)
                r.operation_occurred = True
        r.result_string = ''.join(stack)
        return r

    def calculate(self, expr):
        print("They want us to calculate:", expr)
        r = self.CalcResult(False, expr)
        while True:
            #print(r.result_string) ###
            r = self.open_single_paren(r.result_string)
            if not r.operation_occurred:
                break
        r.result_string = self.eval_expr_without_parens(r.result_string)
        print("The result is:", r.result_string)


if __name__ == "__main__":
    e = DemoExprEvaluator()
    expr = "13^2+17*(3+7*2)"
    print('eval() function: ',eval(expr))
    e.calculate(expr)

