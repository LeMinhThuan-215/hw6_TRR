def m(s, idx, minLetter):
    if idx == len(s):
        return minLetter
    if s[idx] < minLetter:
        return m(s, idx + 1, s[idx])
    else:
        return m(s, idx + 1, minLetter)

numberStr = str(input())
print(m(numberStr, 1, numberStr[0]))