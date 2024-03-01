from calculate import main as calc_expr


def main() -> None:
    global oper_1
    oper_1 = '13x13+23/2'
    print(oper_1, res_1 := eval(oper_1.replace('x', '*')))
    return res_1


def value_test(res_1: int)-> None:
    try:
        assert res_1+1 == (r:=calc_expr(oper_1))[1], f'{res_1} not equal to {r}'
    except AssertionError as err:
        print('\t',  err)


def exception_test() -> None:
    def assert_raises(expected_err, func, *args) -> None:
        try:
            func(args)
        except expected_err:
            print('Error raised succesfuly')
            return True
        except Exception:
            return False
    try:
        assert assert_raises(err:=SyntaxError,
                                calc_expr,
                                'NOT AN OPERATION'
                            ), f'Not expected {err} raised'
    except AssertionError as unexpected_err:
        print(unexpected_err)



if __name__ == "__main__":
    result = main()
    value_test(result)
    exception_test(result)
