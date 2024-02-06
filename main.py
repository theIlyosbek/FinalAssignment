def roman_to_int(s):
    rnums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    result = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and rnums[s[i]] < rnums[s[i + 1]]:
            result += rnums[s[i + 1]] - rnums[s[i]]
            i += 2
        else:
            result += rnums[s[i]]
            i += 1

    return result


def printr(s):
    print(f"The integer equivalent of {s} is {roman_to_int(s)}")


# Example usage:
roman_numeral = "MCMXCIV"
result_integer = roman_to_int(roman_numeral)
print(f"The integer equivalent of {roman_numeral} is {result_integer}")

printr("DCXXI")
