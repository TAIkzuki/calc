import calc
import history

if __name__ == "__main__":
    e = calc.DemoExprEvaluator()
    h = history.History(3)
    expr = "13^2+17*(3+7*2)"
    result = e.calculate(expr)

    push_result=expr+'='+str(result)
    h.push(push_result)
    h.show()
    print('eval function: ',eval(expr))

