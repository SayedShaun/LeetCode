def reverseWords(s):
    res = ""
    for i in s.split(" "):
        res += i[::-1] + " "
    return res.strip()


s = "Let's take LeetCode contest"
print(reverseWords(s))
