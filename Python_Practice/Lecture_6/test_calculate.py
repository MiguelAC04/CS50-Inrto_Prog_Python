from calculate import main as calc_expr


def main() -> None:
    oper_1 = '13x13+23/2'
    print(oper_1, res_1 := eval(oper_1.replace('x', '*')))
    try:
        assert res_1 == (r:=calc_expr(oper_1))[1]
    except AssertionError:
        print(f'Wrong answer for function: {res_1} vs {r}')


if __name__ == "__main__":
    main()
