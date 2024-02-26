import calculate


def main() -> None:
    oper_1 = '13x13+23/2'
    print(oper_1, res_1 := eval(oper_1.replace('x', '*')))
    try:
        assert res_1 == calculate.main(oper_1)
    except AssertionError:
        print('Wrong answer for function')


if __name__ == "__main__":
    main()
