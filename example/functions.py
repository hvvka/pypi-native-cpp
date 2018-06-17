import better_than_python


def factorial(number):
    """
    Recursive function that calculates the factorial of the given number.

    :return a number (factorial)
    """
    if not isinstance(number, int):
        raise Exception('Enter an integer number to find the factorial')

    return int(better_than_python.factorial(number))


def is_palindrome(string):
    """
    Checks the string for palindrome.

    :param string: string to check
    :return true if string is a palindrome false if not
    """
    if string == string[::-1]:
        return True
    return False


if __name__ == '__main__':
    number = input("Enter number: ")
    print(factorial(int(number)))
