from twos_complement import twos_complement



def bi_to_dec(binary):
    # Initialize variables
    integer = binary
    decimal = 0

    # Check if the binary number contains a decimal point
    if '.' in binary:
        # If it does, handle the decimal part separately
        decimal_point = 0.0
        integer, decimal_part = integer.split('.')

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
        return decimal + decimal_point

    else:
        return decimal


def binary_to_decimal(binary):
     if binary[0] == '1':
        decimal = -bi_to_dec(twos_complement(binary))
        return decimal
     else:
        decimal = bi_to_dec(binary)
        return decimal


def binary_to_octal(binary):
    # Initialize variables
    integer = binary

    # Check if the binary number contains a decimal point
    if '.' in binary:
        # If it does, split the binary number into integer and decimal parts
        integer, decimal = integer.split('.')

        # Reverse the decimal part of the binary number

        # Pad the decimal part with zeros until its length is a multiple of 3
        while len(decimal) % 3 != 0:
            decimal = decimal + '0'

        # Initialize a variable to store the octal equivalent of the decimal part
        dec_octal = ''

        # Convert the decimal part to octal by grouping digits into sets of three and converting each set to decimal
        for i in range(0, len(decimal), 3):
            temp = decimal[i:i + 3]
            dec_octal += str(int(bi_to_dec(temp)))

    # Pad the integer part with zeros until its length is a multiple of 3
    if integer[0] == '1':
        while len(integer) % 3 != 0:
            integer = '1' + integer
        if integer[:3] != '111':
            integer = '111' + integer
    else:
        integer = integer.lstrip('0')
        while len(integer) % 3 != 0:
            integer = '0' + integer
    # Initialize a variable to store the octal equivalent of the integer part
    octal = ''

    # Convert the integer part to octal by grouping digits into sets of three and converting each set to decimal
    for i in range(0, len(integer), 3):
        temp = integer[i:i + 3]
        octal += str(int(bi_to_dec(temp)))

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
            temp_dec = int(bi_to_dec(temp))
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
        if integer[:4] != '1111':
            integer = '1111' + integer
    else:
        while len(integer) % 4 != 0:
            integer = '0' + integer

    # Initialize a variable to store the hexadecimal equivalent of the integer part
    hexadecimal = ''

    # Convert the integer part to hexadecimal by grouping digits into sets of four and converting each set to decimal
    for i in range(0, len(integer), 4):
        temp = integer[i:i + 4]
        temp_dec = int(bi_to_dec(temp))
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


