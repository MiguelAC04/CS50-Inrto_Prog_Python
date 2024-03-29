from calculate import main as calc_expr
from pytest import raises as pytest_raises

oper_1 = '13x13+23/2'
print(oper_1, res_1 := eval(oper_1.replace('x', '*')))


def test_values():
    '''Test 1'''
    assert res_1 == (r:=calc_expr(oper_1))[1], f'{res_1} not equal to {r}'


def test_operator_exception():
    '''Test 2'''
    test, msg = raises(SyntaxError, calc_expr, '90¨¨30__12')
    assert test, msg


def test_value_exeption():
    '''Tests 3'''
    # test, msg = raises(ValueError, calc_expr, '3xa+2x+2')
    # assert test, msg
    with pytest_raises(SyntaxError):
        calc_expr('3xa+2x+2')


def test_operator_combination():
    '''Test 4'''
    assert raises(None, calc_expr, '12/+1+3*-1')


def raises(expected_err, func, *args):
    if expected_err:
        try:
            func(*args)
        except expected_err:
            return True, 'Succesful raise'
        except Exception:
            return False, 'Unexpected Error'
        else:
            return False, 'No error raised'
    else:
        try:
            func(*args)
        except Exception:
            raise AssertionError
        else:
            return True
def test_f():
    print('\n\n\t\t\tTHIS FUNCTION WAS ALSO CALLED\n\n')
    assert False
