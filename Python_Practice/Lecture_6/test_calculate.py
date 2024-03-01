from calculate import main as calc_expr


def main() -> None:
    oper_1 = '13x13+23/2'
    print(oper_1, res_1 := eval(oper_1.replace('x', '*')))

    def value_test()-> None:
        try:
            assert res_1 == (r:=calc_expr(oper_1))[1], f'{res_1} not = to {r}'
        except AssertionError as err:
            print('\t',  err)
            raise

    def exception_test() -> None:

        def assert_raises(err, func, *args) -> None:
            try:
                func(args)
            except err:
                print('Error raised succesfuly')
            except Exception:
                return False

        try:
            assert assert_raises(SyntaxError, calc_expr, 'NOT AN OPERATION')
        except AssertionError as syn_err:
            print('No SyntaxError raised:', syn_err)

    value_test()
    exception_test()



if __name__ == "__main__":
    main()
