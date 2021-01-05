def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'

    if n % 3 == 0:
        return 'Fizz'

    if n % 5 == 0:
        return 'Buzz'

    return str(n)


def main():
    for i in range(1, 100):
        message = fizzbuzz(i)
        print(message)


if __name__ == '__main__':
    main()
