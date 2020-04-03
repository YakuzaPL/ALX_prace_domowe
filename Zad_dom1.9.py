def number_generator():
    generator = range(1, 100)

    return generator


def main():
    generator = number_generator()

    for number in generator:
        if number % 15 == 0:
            print(number, end=" ")
            print("FizzBizz")
        elif number % 5 == 0:
            print(number, end=" ")
            print("Bizz")
        elif number % 3 == 0:
            print(number, end=" ")
            print("Fizz")


main()
