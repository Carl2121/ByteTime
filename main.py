import binary_addition, binary_subtraction, binary_multiplication, binary_division


def main():
    while True:
        print("\nMain Menu:")
        print("1. Binary Operations")
        print("2. Number System Conversion")
        print("3. Exit")

        choice = input("\nPlease choose an option: ")

        if choice == '1':
            while True:
                print("\nMenu-2 (Binary Operations):")
                print("1. Division")
                print("2. Multiplication")
                print("3. Subtraction")
                print("4. Addition")
                print("5. Negative (2's Complement)")
                print("6. Back to Main Menu")

                choice = input("\nPlease choose an option: ")

                if choice == '6':
                    break
                else:
                    print("\nYou chose Option", choice)
                    # code

        elif choice == '2':
            while True:
                print("\nMenu-3 (Conversion):")
                print("1. Binary to X")
                print("2. Decimal to X")
                print("3. Octal to X")
                print("4. Hexa to X")
                print("5. Back to Main Menu")

                choice = input("\nPlease choose an option: ")

                if choice == '5':
                    break
                else:
                    print("\nYou chose Option", choice)
                    # code

        elif choice == '3':
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()