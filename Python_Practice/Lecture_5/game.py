from random import randint


def main() -> None:
    while True:
        if (num:=input('Level: ')).isdigit():
            rand_num = randint(1, int(num))
            check_Guess(rand_num)


def check_Guess(rand_num: int) -> None:
    while True:
        if (guess:=input('Guess: ')).isdigit():
            guess = int(guess)
            if guess == rand_num:
                exit('Just Right!')
            elif guess < rand_num:
                print('Too Low!')
            else:
                print('Too High!')


main()