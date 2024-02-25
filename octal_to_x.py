from B1nary_to_X import binary_to_decimal, binary_to_hex
from twos_complement import twos_complement


def octal_to_binary(octal):
    binary = ""
    integer = octal

    if '.' in integer:
        integer, decimal = integer.split('.')
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


def octal_to_decimal(octal):
    binary = octal_to_binary(octal)
    if octal[0] == '7':
        decimal = -binary_to_decimal(twos_complement(binary))
        return decimal
    else:
        decimal = binary_to_decimal(binary)
        return decimal


def octal_to_hex(octal):
    binary = octal_to_binary(octal)

    if octal[0] == '7':
        while len(binary) % 4 != 0:
            binary = '1' + binary

        hex = binary_to_hex(binary)
        return hex

    else:
        hex = binary_to_hex(binary)
        return hex


# Example usage:
#octal = '75'
#print(octal_to_binary(octal))
#print(octal_to_decimal(octal))
#print(octal_to_hex(octal))
