from B1nary_to_X import binary_to_decimal, binary_to_octal
from twos_complement import twos_complement


def hex_to_binary(hexadecimal):
    binary_result = ""
    integer = hexadecimal
    hex_chars = "0123456789ABCDEF"
    hex_values = {}

    if '.' in integer:
        integer, decimal = integer.split('.')
        hexa_dec = ""
        for i in range(len(hex_chars)):
            hex_values[hex_chars[i]] = i

        for digit in decimal:
            if digit.isdigit():
                value = int(digit)
            elif digit.upper() in hex_chars:
                value = hex_values[digit.upper()]
            else:
                raise ValueError("Invalid hexadecimal digit: " + digit)

            binary_digit = ""
            while value:
                binary_digit = str(value % 2) + binary_digit
                value //= 2

            while len(binary_digit) < 4:
                binary_digit = '0' + binary_digit

            hexa_dec += binary_digit

        hexa_dec = hexa_dec.lstrip('0')

    for i in range(len(hex_chars)):
        hex_values[hex_chars[i]] = i

    for digit in integer:
        if digit.isdigit():
            value = int(digit)
        elif digit.upper() in hex_chars:
            value = hex_values[digit.upper()]
        else:
            raise ValueError("Invalid hexadecimal digit: " + digit)

        binary_digit = ""
        while value:
            binary_digit = str(value % 2) + binary_digit
            value //= 2

        while len(binary_digit) < 4:
            binary_digit = '0' + binary_digit

        binary_result += binary_digit

    if '.' in hexadecimal:
        binary_result = binary_result.lstrip('0')
        hexa_dec = hexa_dec.rstrip("0")
        return binary_result + '.' + hexa_dec
    else:
        binary_result = binary_result.lstrip('0')
        return binary_result


def hex_to_decimal(hex):
    binary = hex_to_binary(hex)
    if binary[0] == '1':
        return -binary_to_decimal(twos_complement(binary))
    else:
        return binary_to_decimal(binary)


def hex_to_octal(hex):
    binary = hex_to_binary(hex)

    return binary_to_octal(binary)


hex = 'ff6'
print(hex_to_binary(hex))
print(hex_to_decimal(hex))
print(hex_to_octal(hex))