from calculate import main as calc_expr


oper_1 = '13x13+23/2'
print(oper_1, res_1 := eval(oper_1.replace('x', '*')))


def test_values():
    assert res_1+1 == (r:=calc_expr(oper_1))[1], f'{res_1} not = to {r}'

def test_exception():
    def raises(expected_err, func, *args):
        try:
            func(*args)
        except expected_err:
            return True, 'Succesful raise'
        except Exception:
            return False, 'Unexpected Erro'
        else:
            return False, 'No error raised'

    test, msg = raises(SyntaxError, calc_expr, 'Not a numerical expression')
    assert test, msg


