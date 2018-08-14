def is_palindrome(argument):
    if argument == argument[::-1]:
        return True
    return False

if __name__ == '__main__':
    value = input('Enter a value please:',)
    print(is_palindrome(value))