from misc.fraction import decimal_to_fraction
def polynomial_long_division(dividend, divisor):
    if len(divisor) > len(dividend):
        raise ValueError("Degree of divisor must be less than or equal to the degree of dividend")

    quotient = [0] * (len(dividend) - len(divisor) + 1)
    while len(dividend) >= len(divisor):
        leading_coefficient = dividend[0] / divisor[0]
        quotient[len(dividend) - len(divisor)] = leading_coefficient

        for i in range(len(divisor)):
            dividend[i] -= leading_coefficient * divisor[i]

        dividend = [coef for coef in dividend if coef != 0]

    remainder = dividend

    return quotient, remainder


def synthetic_division(dividend, divisor):
    if len(divisor) > len(dividend):
        raise ValueError("Degree of divisor must be less than or equal to the degree of dividend")

    quotient = [0] * (len(dividend) - len(divisor) + 1)
    remainder = dividend.copy()

    for i in range(len(dividend) - len(divisor) + 1):
        quotient[i] = remainder[0] / divisor[0]
        print(quotient)
        for j in range(len(divisor)):
            remainder[i + j] -= quotient[i] * divisor[j]

    return quotient, remainder

def print_polynomial(coefficients, decimal_points):
    degree = len(coefficients) - 1
    polynomial = ""

    for i, coef in enumerate(coefficients):
        power = degree - i
        if coef != 0:
            if polynomial:
                polynomial = " + " + polynomial if coef > 0 else " - " + polynomial
            else:
                if coef < 0:
                    polynomial += "-"

            coef = abs(coef)
            if coef != 1 or power == 0:
                formatted_coef = f"{coef:.{decimal_points}f}" if coef != int(coef) else str(int(coef))
                polynomial += formatted_coef

            if power > 0:
                polynomial += f"x"
                if power > 1:
                    polynomial += f"^{power}"

    if polynomial:
        print(polynomial)
    else:
        print("0")



def print_fraction_as_polynomial(numerator, denominator, degree):
    if numerator == 0:
        return "0"
    elif denominator == 1:
        return f"{numerator}x^{degree}"
    else:
        return f"{numerator}x^{degree}/{denominator}"

def main():
    print("Polynomial Long Division Program")
    dividend = list(map(float, input("Enter the coefficients of the dividend (highest degree first): ").split()))
    divisor = list(map(float, input("Enter the coefficients of the divisor (highest degree first): ").split()))
    final_string = ""
    try:
        if len(divisor) == 1:
            quotient, remainder = synthetic_division(dividend, divisor)
            if input("Do you want to see the quotient in fraction form? (y/n): ").strip().lower() == 'y':
                print("Quotient:")
                for i, coef in enumerate(quotient):
                    numerator, denominator = decimal_to_fraction(coef)
                    print(print_fraction_as_polynomial(numerator, denominator, len(quotient) - 1 - i))
                print("Remainder:")
                print(str(decimal_to_fraction(remainder[0])[0]) + "/" + str(decimal_to_fraction(remainder[0])[1]))
            else:
                ask = int(input("How many decimals (int): "))
                print_polynomial(quotient, ask)
                print("remainder: ")
                print_polynomial(remainder, ask)

        else:
            quotient, remainder = polynomial_long_division(dividend, divisor)
            if input("Do you want to see the quotient in fraction form? (y/n): ").strip().lower() == 'y':
                print("Quotient:")
                for i, coef in enumerate(quotient):
                    numerator, denominator = decimal_to_fraction(coef)
                    final_string+=str(print_fraction_as_polynomial(numerator, denominator, len(quotient) - 1 - i)) +" "
                print(final_string)
                print("Remainder:")
                print(str(decimal_to_fraction(remainder[0])[0]) + "/" + str(decimal_to_fraction(remainder[0])[1]))
            else:
                ask = int(input("How many decimals (int): "))
                print_polynomial(quotient, ask)
                print("remainder: ")
                print_polynomial(remainder, ask)



    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
