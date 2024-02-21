from twos_complement import twos_complement, validate_binary_string
from binary_to_x import binary_to_decimal
from decimal_to_x import binary


def binary_to_nibble(binary: str = None, bit: int = 4):
    binary_array = [binary, None] if '.' not in binary else binary.split('.')
    binary = ' '.join([binary_array[0][max(i-bit, 0):i] for i in range(len(binary_array[0]), 0, -bit)][::-1])

    if binary_array[1] is not None:
        binary = f'{binary}.{" ".join([binary_array[1][i:i+bit] for i in range(0, len(binary_array[1]), bit)])}'
    return binary

def binary_addition(binary1:str, binary2:str) -> str:
    validate_binary_string(binary1)
    validate_binary_string(binary2)

    bin1 = binary_to_decimal(binary1) if binary1[0] != '1' else -binary_to_decimal(twos_complement(binary1))
    bin2 = binary_to_decimal(binary2) if binary2[0] != '1' else -binary_to_decimal(twos_complement(binary2))

    result = bin1 + bin2

    if result < 0:
        #convert it to its absolute value in binary, then convert back to its two's complement
        result_binary = twos_complement(binary(abs(result)))
        result_binary = result_binary.rjust(12, '1')
    else:
        result_binary = binary(result)
        result_binary = result_binary.zfill(12)

    return binary_to_nibble(result_binary)

if __name__ == '__main__':
    binary1 = input("Enter the first binary number: ")
    binary2 = input("Enter the second binary number: ")
    result = binary_addition(binary1, binary2)
    print(result)
