from twos_complement import twos_complement
from twos_complement import validate_binary_string


def binary_addition(binary1:str, binary2:str) -> str:
    validate_binary_string(binary1)
    validate_binary_string(binary2)

    if binary1[0] == "1":
        twos_complement(binary1)
        pass
    else:
        pass
