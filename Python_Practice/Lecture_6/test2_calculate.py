from calculate import main as calc_expr


oper_1 = '13x13+23/2'
print(oper_1, res_1 := eval(oper_1.replace('x', '*')))


def test_values():
    assert res_1+1 == (r:=calc_expr(oper_1))[1], f'{res_1} not equal to {r}'



def test_operator_exception():
    test, msg = raises(SyntaxError, calc_expr, '90¨¨30__12')
    assert test, msg

def test_value_exeption():
    test, msg = raises(ValueError, calc_expr, '3xa+2x+2')
    assert test, msg

def test_operator_combination():
    assert 

def raises(expected_err, func, *args):
        try:
            func(*args)
        except expected_err:
            return True, 'Succesful raise'
        except Exception:
            return False, 'Unexpected Error'
        else:
            return False, 'No error raised'
