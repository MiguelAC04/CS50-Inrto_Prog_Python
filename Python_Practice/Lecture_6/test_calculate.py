from calculate import main as calc_expr


def main() -> None:
    oper_1 = '13x13+23/2'
    print(oper_1, res_1 := eval(oper_1.replace('x', '*')))

    def value_test()->None:
        try:
            assert res_1 == (r:=calc_expr(oper_1))[1], f'{res_1} not = to {r}'
        except AssertionError as err:
            print('\t',  err)
            raise
    def exception_test() -> None:
        def asser_raises() -> None:
            
        try:
            assert_raises(SyntaxError, main, 'NOT AN OPERATION'),
            'Does not raise SyntaxError when invalid syntax is recieved'
        except AssertionError as syn_err:
            print(syn_err)
    value_test()
    exception_test()



if __name__ == "__main__":
    main()
