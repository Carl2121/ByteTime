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



