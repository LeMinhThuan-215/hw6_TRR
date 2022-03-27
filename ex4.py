def reverseStr(s, ans, i):
    if i == len(s):
        return ans
    ans = s[i] + ans
    return reverseStr(s, ans, i+1)

string = str(input())
ans = ""
ans = reverseStr(string, ans, 0)
print(ans)