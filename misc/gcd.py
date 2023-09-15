def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    nums = list(map(float, input("Enter the two numbers: ").split()))
    print(f"GCD is {gcd(nums[0], nums[1])}")


if __name__ == "__main__":
    main()
