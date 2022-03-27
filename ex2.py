def ones(s, idx):
    if idx == len(s):
        return 0
    if s[idx] == "1":
        return 1 + ones(s, idx + 1)
    else:
        return ones(s, idx + 1)

binaryStr = str(input())
print(ones(binaryStr, 0))
