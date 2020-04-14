def main():
    for number in range(1, 100):
        if number % 15 == 0:
            print(number, end=" ")
            print("FizzBizz")
        elif number % 5 == 0:
            print(number, end=" ")
            print("Bizz")
        elif number % 3 == 0:
            print(number, end=" ")
            print("Fizz")
        else:
            print(number)


main()
