"""Vanessa Calimag"""


def main():
    password = input("Enter a password: ")
    if len(password) < 10:
        print("Minimum number of characters is 10 - Enter a password.")
    else:
        print('*').format(password)


main()
