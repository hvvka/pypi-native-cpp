

def factorial(number):
    """
    Recursive function that calculates the factorial of the given number.

    :return a number (factorial)
    """
    if not isinstance(number, int):
        raise Exception('Enter an integer number to find the factorial')
    if number == 1 or number == 2:
        return 1
    else:
        return number * factorial(number - 1)


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
    print(factorial(10))
    print(is_palindrome("dppd"))
