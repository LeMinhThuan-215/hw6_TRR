def sinh(s, open):
    if (len(s) > n):
        return
    if (open == 0):
        print(s)
    sinh(s + '(', open + 1)
    if (open > 0):
        sinh(s + ')', open - 1)

n = int(input())
while n % 2 == 1:
    n = int(input())
sinh("", 0)