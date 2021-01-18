def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)


def lcm(a, b):
    gcd_value = gcd(a, b)
    if (gcd_value == 0):
        return 0
    return abs( (a * b) / gcd_value )
