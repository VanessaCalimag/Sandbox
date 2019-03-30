
MENU = """L - List places
A - Add new place
M - Mark a place as visited
Q - Quit"""
PLACES = 'test.csv'


def main():
    input_file = open(PLACES, 'r')
    input_data = input_file.readlines()
    places_value = []
    for line in input_data:
        parts = line.strip().split(',')
        places = [parts[0], parts[1], parts[2] in parts]  # need to edit, research more for the format
        places_value.append(places)
        print(places)  # remove once done to follow recommended output
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            # TODO create function to list out the places
            print("LOL")
        elif choice == "A":
            # TODO create function to add places to the list
            print("Sad")
        elif choice == "M":
            # TODO create function to mark place as visited
            print("Happy")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    input_file.close()
    print("Have a nice day!")


main()
