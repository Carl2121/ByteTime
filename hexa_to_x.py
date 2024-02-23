from binary_to_x import binary_to_decimal, binary_to_octal

def hex_to_binary(hexadecimal):
    binary_result = ""
    integer = hexadecimal
    hex_chars = "0123456789ABCDEF"
    hex_values = {}

    if '.' in hexadecimal:
        integer, decimal = hexadecimal.split('.')
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

    binary_result = binary_result.lstrip('0')

    if '.' in hexadecimal:
        hexa_dec = hexa_dec.rstrip("0")
        return binary_result + '.' + hexa_dec
    else:
        return binary_result

def main():
    hexadecimal_number = input("Enter a hexadecimal number: ").upper()
    binary_result = hex_to_binary(hexadecimal_number)
    print(f"Binary: {binary_result} \nDecimal: {binary_to_decimal(binary_result)} \nOctal: {binary_to_octal(binary_result)}")

if __name__ == "__main__":
    main()