def gcd(a, b):
    if b == 0:
        return a
    if a > b:
        return gcd(b, a)
    if a%2 == 0 and b%2 == 0:
        return 2*gcd(a/2, b/2)
    if (a%2 == 0 and b%2 == 1):
        return gcd(a/2, b)
    return gcd(a, b-a)

number1 = int(input())
number2 = int(input())
print(int(gcd(number1, number2)))