def find_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + (discriminant)**0.5) / (2*a)
        root2 = (-b - (discriminant)**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root1 = -b / (2*a)
        return root1
    else:
        real_part = -b / (2*a)
        imaginary_part = ((-discriminant)**0.5) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

def main():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))
    roots = find_quadratic_roots(a, b, c)
    if isinstance(roots, tuple):
        print(f"Root 1: {roots[0]}")
        print(f"Root 2: {roots[1]}")
    else:
        print(f"Root: {roots}")

if __name__ == "__main__":
    main()
