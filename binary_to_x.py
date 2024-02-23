from twos_complement import twos_complement


def binary_to_decimal(binary:str)-> int| float:
    # Initialize variables
    integer = binary
    decimal = 0

    # Check if the binary number is negative
    if binary[0] == '1':
        binary = twos_complement(binary)
        is_negative = True
    else:
        is_negative = False

    # Check if the binary number contains a decimal point
    if '.' in binary:
        # If it does, handle the decimal part separately
        decimal_point = 0.0
        integer, decimal_part = binary.split('.')

        # Convert the decimal part to decimal using the binary_to_decimal function
        for i in range(len(decimal_part)):
            if decimal_part[i] == '1':
                decimal_point += 2 ** (-(i + 1))

    # Reverse the integer part of the binary number
    integer = integer[::-1]

    # Convert the integer part to decimal
    for i in range(len(integer)):
        if integer[i] == '1':
            decimal += 2 ** i

    # If the binary number had a decimal point, add the decimal part to the integer part
    if '.' in binary:
        decimal += decimal_point

    # If the binary number was negative, return the negative of the decimal
    if is_negative:
        return -decimal
    else:
        return decimal

def binary_to_octal(binary):
    # Initialize variables
    integer = binary

    # Check if the binary number contains a decimal point
    if '.' in binary:
        # If it does, split the binary number into integer and decimal parts
        integer, decimal = binary.split('.')

        # Reverse the decimal part of the binary number
        decimal = decimal[::-1]

        # Pad the decimal part with zeros until its length is a multiple of 3
        while len(decimal) % 3 != 0:
            decimal = '0' + decimal

        # Initialize a variable to store the octal equivalent of the decimal part
        dec_octal = ''

        # Convert the decimal part to octal by grouping digits into sets of three and converting each set to decimal
        for i in range(0, len(decimal), 3):
            temp = decimal[i:i + 3]
            dec_octal += str(int(binary_to_decimal(temp)))

    # Pad the integer part with zeros until its length is a multiple of 3
    if integer[0] == '1':
        while len(integer) % 4 != 0:
            integer = '1' + integer
        integer = '1111' + integer
    else:
        while len(integer) % 4 != 0:
            integer = '0' + integer
        integer = '0000' + integer

    # Initialize a variable to store the octal equivalent of the integer part
    octal = ''

    # Convert the integer part to octal by grouping digits into sets of three and converting each set to decimal
    for i in range(0, len(integer), 3):
        temp = integer[i:i + 3]
        octal += str(int(binary_to_decimal(temp)))

    # If the binary number had a decimal point, return the octal representation with the decimal point
    if '.' in binary:
        return octal + '.' + dec_octal
    else:
        return octal


def binary_to_hex(binary):
    # Initialize variables
    hex_chars = "0123456789ABCDEF"
    integer = binary

    # Check if the binary number contains a decimal point
    if '.' in binary:
        # If it does, split the binary number into integer and decimal parts
        integer, decimal = binary.split('.')

        # Pad the decimal part with zeros until its length is a multiple of 4
        while len(decimal) % 4 != 0:
            decimal = decimal + '0'

        # Initialize a variable to store the hexadecimal equivalent of the decimal part
        dec_hex = ''

        # Convert the decimal part to hexadecimal by grouping digits into sets of four and converting each set to decimal
        for i in range(0, len(decimal), 4):
            temp = decimal[i:i + 4]
            temp_dec = int(binary_to_decimal(temp))
            temp_hex = ""

            # Convert the decimal value to hexadecimal
            while temp_dec:
                temp_hex = hex_chars[temp_dec % 16] + temp_hex
                temp_dec //= 16
            dec_hex += temp_hex

    # Pad the integer part with zeros until its length is a multiple of 4
    if integer[0] == '1':
        while len(integer) % 4 != 0:
            integer = '1' + integer
        integer = '1111' + integer
    else:
        while len(integer) % 4 != 0:
            integer = '0' + integer
        integer = '0000' + integer

    # Initialize a variable to store the hexadecimal equivalent of the integer part
    hexadecimal = ''

    # Convert the integer part to hexadecimal by grouping digits into sets of four and converting each set to decimal
    for i in range(0, len(integer), 4):
        temp = integer[i:i + 4]
        temp_dec = int(binary_to_decimal(temp))
        temp_hex = ""

        # Convert the decimal value to hexadecimal
        while temp_dec:
            temp_hex = hex_chars[temp_dec % 16] + temp_hex
            temp_dec //= 16
        hexadecimal += temp_hex

    # If the binary number had a decimal point, return the hexadecimal representation with the decimal point
    if '.' in binary:
        return hexadecimal + '.' + dec_hex
    else:
        return hexadecimal

def main():
    # Prompt the user to enter a binary number
    binary_number = input("Enter a binary number: ")

    # Convert the binary number to decimal
    if binary_number[0] == '1':
        decimal_result = -binary_to_decimal(twos_complement(binary_number))
    else:
        decimal_result = binary_to_decimal(binary_number)
    print(f"Decimal: {decimal_result}")

    # Convert the binary number to octal
    octal_result = binary_to_octal(binary_number)
    if octal_result[0] == '1':
        octal_result = '-' + octal_result[1:]
    print(f"Octal: {octal_result}")

    # Convert the binary number to hexadecimal
    hex_result = binary_to_hex(binary_number)
    if hex_result[0] == '1':
        hex_result = '-' + hex_result[1:]
    print(f"Hexadecimal: {hex_result}")

if __name__ == "__main__":
    main()