import calc
import history

if __name__ == "__main__":
    e = calc.DemoExprEvaluator()
    h = history.History(3)
    expr = "13^2+17*(3+7*2)"


    print('eval function: ',eval(expr))
    e.calculate(expr)
