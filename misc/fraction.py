from misc.gcd import gcd
def decimal_to_fraction(decimal):
    num = int(decimal * 1000000)
    denom = 1000000

    common_divisor = gcd(num, denom)
    num /= common_divisor
    denom /= common_divisor

    return int(num), int(denom)

def main():
    final = decimal_to_fraction(float(input("Enter decimal: ")))
    print(f"Fraction is {final[0]}/{final[1]}")


if __name__ == "__main__":
    main()
