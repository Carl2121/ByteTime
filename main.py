import binary_addition, binary_subtraction, binary_multiplication, binary_division
from B1nary_to_X import binary_to_decimal, binary_to_octal, binary_to_hex
from decimal_to_x import decimal_to_binary_signed, decimal_to_octal, decimal_to_hex
from octal_to_x import octal_to_binary, octal_to_decimal, octal_to_hex
from hexa_to_x import hex_to_binary, hex_to_decimal, hex_to_octal
from twos_complement import twos_complement

def main():
    while True:
        print("\nMain Menu:")
        print("[1] Binary Operations")
        print("[2] Number System Conversion")
        print("[3] Exit")

        choice = input("\nPlease choose an option: ")

        if choice == '1':
            while True:
                print("\nMenu-2 (Binary Operations):")
                print("[1] Division")
                print("[2] Multiplication")
                print("[3] Subtraction")
                print("[4] Addition")
                print("[5] Negative (2's Complement)")
                print("[6] Back to Main Menu")


                choice = input("\nPlease choose an option: ")

                if choice == '6':
                    break
                elif choice == '5':
                    binary1 = input("Enter the binary number: ")
                    print(twos_complement(binary1))
                else:
                    binary1 = input("Enter the first binary number: ")
                    binary2 = input("Enter the second binary number: ")

                    if choice == '1':
                        print(binary_division.binary_division(binary1, binary2))
                    elif choice == '2':
                        print(binary_multiplication.binary_multiplication(binary1, binary2))
                    elif choice == '3':
                        print(binary_subtraction.binary_subtraction(binary1, binary2))
                    elif choice == '4':
                        print(binary_addition.binary_addition(binary1, binary2))

        elif choice == '2':
            while True:
                print("\nMenu-3 (Conversion):")
                print("[1] Binary to X")
                print("[2] Decimal to X")
                print("[3] Octal to X")
                print("[4] Hexa to X")
                print("[5] Back to Main Menu")

                choice = input("\nPlease choose an option: ")

                if choice == '5':
                    break
                else:
                    if choice == '1':
                        binary = input("Input Binary: ")
                        print("Output:")
                        print("Decimal:", binary_to_decimal(binary))
                        print("Octal:", binary_to_octal(binary))
                        print("Hexa:", binary_to_hex(binary))
                    elif choice == '2':
                        decimal = float(input("Input Decimal: "))
                        print("Output:")
                        print("Binary: ", decimal_to_binary_signed(decimal))
                        print("Octal: ", decimal_to_octal(decimal))
                        print("Hexa: ", decimal_to_hex(decimal))
                    elif choice == '3':
                        octal = input("Input Octal: ")
                        print("Output:")
                        print("Binary: ", octal_to_binary(octal))
                        print("Decimal: ", octal_to_decimal(octal))
                        print("Hexa: ", octal_to_hex(octal))
                    elif choice == '4':
                        hexa = input("Input Hexa: ")
                        print("Output:")
                        print("Binary: ", hex_to_binary(hexa))
                        print("Decimal: ", hex_to_decimal(hexa))
                        print("Octal: ", hex_to_octal(hexa))



        elif choice == '3':
            print("\nThanks for Using ByteTime :).")
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()