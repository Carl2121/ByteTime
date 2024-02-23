def twos_input(binary: str = None):
    return input("Enter Binary: ") if binary is None else binary

def validate_binary_string(binary_str) -> int:
    if not set(binary_str).issubset({'0', '1', '.'}):
        raise ValueError("Input must be a binary string")

    n = len(binary_str)

    if n == 0:
        raise ValueError("Binary string cannot be empty")

    return n

def binary_to_nibble(binary: str = None, bit: int = 4):
    binary_array = [binary, None] if '.' not in binary else binary.split('.')
    binary = ' '.join([binary_array[0][max(i-bit, 0):i] for i in range(len(binary_array[0]), 0, -bit)][::-1])

    if binary_array[1] is not None:
        binary = f'{binary}.{" ".join([binary_array[1][i:i+bit] for i in range(0, len(binary_array[1]), bit)])}'
    return binary


def twos_complement(binary_str: str) -> str:

    n = validate_binary_string(binary_str)
    decimal_position = binary_str.find('.')

    # perform 2s complement kung walang decimal point
    if decimal_position == -1:
        inverted_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        inverted_int = int(inverted_str, 2) #what if i use binary_to_decimal() here?
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
