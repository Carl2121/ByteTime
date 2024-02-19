from twos_complement import twos_complement
from twos_complement import validate_binary_string
from binary_to_x import binary_to_decimal
from decimal_to_x import binary


def binary_addition(binary1:str, binary2:str) -> str:
    validate_binary_string(binary1)
    validate_binary_string(binary2)

    if binary2[0] == "1":
        twos_bin = twos_complement(binary2)
        bin2 = binary_to_decimal(twos_bin)
        bin1 = binary_to_decimal(binary1)
        answer = bin1 + (-bin2)
        if answer > 0:
            final = binary(answer)
            # Pad the final result with zeros up to 12 bits
            final = final.zfill(12)
        return final
    else:
        pass


print(binary_addition("0110.11", "1101.11"))