from binary_to_x import binary_to_decimal, binary_to_hex


def octal_to_binary(octal):
    binary = ""
    integer = octal

    if '.' in octal:
        integer, decimal = octal.split('.')
        dec_bi = ""
        for x in decimal:
            digit = ""
            num = int(x)
            for i in range(3):
                digit = str(num % 2) + digit
                num //= 2
            dec_bi += digit
        if not dec_bi:
            dec_bi = '0'

    for x in integer:
        digit = ""
        num = int(x)
        for i in range(3):
            digit = str(num % 2) + digit
            num //= 2
        binary += digit
    if not binary:
        binary = '0'

    if '.' in octal:
        binary = binary.lstrip('0')
        dec_bi = dec_bi.rstrip('0')
        return binary + '.' + dec_bi
    else:
        binary = binary.lstrip('0')
        return binary


# Example usage:
def main():
    # Prompt the user to enter an octal number
    octal_number = input("Enter an octal number: ")

    # Convert the octal number to binary
    binary_result = octal_to_binary(octal_number)
    print(f"Binary: {binary_result}")

    # Convert the binary number to decimal
    decimal_result = binary_to_decimal(binary_result)
    print(f"Decimal: {decimal_result}")

    # Convert the binary number to hexadecimal
    hex_result = binary_to_hex(binary_result)
    print(f"Hexadecimal: {hex_result}")

if __name__ == "__main__":
    main()