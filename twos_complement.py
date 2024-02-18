def twos_input(binary: str = None):
    return input("Enter Binary: ") if binary is None else binary


def twos_complement(binary_str: str) -> str:
    if not set(binary_str).issubset({'0', '1', '.'}):
        raise ValueError("Input must be a binary string")

    n = len(binary_str)

    if n == 0:
        raise ValueError("Binary string cannot be empty")

    decimal_position = binary_str.find('.')

    # perform 2s complement kung walang decimal point
    if decimal_position == -1:
        inverted_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        inverted_int = int(inverted_str, 2)
        twos_complement_int = inverted_int + 1
        twos_complement_str = format(twos_complement_int, '0' + str(n) + 'b')
    else:
        # Kung may decimal, remove temporarily and perform 2s complement at reinsert decimal
        integer_and_fractional = binary_str.replace('.', '')
        inverted_str = ''.join('1' if bit == '0' else '0' for bit in integer_and_fractional)
        inverted_int = int(inverted_str, 2)
        twos_complement_int = inverted_int + 1
        twos_complement_str = format(twos_complement_int, '0' + str(len(integer_and_fractional)) + 'b')

        twos_complement_str = twos_complement_str[:decimal_position] + '.' + twos_complement_str[decimal_position:]

    return twos_complement_str

if __name__ == '__main__':
    val = twos_input()
    print(twos_complement(val))
