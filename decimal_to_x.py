def binary(num):
    whole = int(num)
    fraction = num - whole

    binary_whole = to_binary_whole(whole)
    binary_fraction = to_binary_fraction(fraction)

    if binary_fraction:
        return f'{binary_whole}.{binary_fraction}'
    else:
        return f"{binary_whole}"


def to_binary_whole(num):
    binary_array = []
    while num > 0:
        mod = num % 2
        num = num // 2
        binary_array.append(str(mod))
    return "".join(reversed(binary_array))


def to_binary_fraction(fraction):
    binary = ""
    max_iterations = 10

    while max_iterations > 0:
        if fraction == 0:
            break

        fraction *= 2
        if fraction >= 1:
            binary += '1'
            fraction -= 1
        else:
            binary += '0'

        max_iterations -= 1

    return binary

