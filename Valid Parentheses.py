def isValid(s):
    my_dict = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for i in s:
        if i in my_dict.keys():
            stack.append(i)
        if i in my_dict.values():
            if not stack or i != my_dict[stack.pop()]:
                return False
    return len(stack) == 0


s = "()"
print(isValid(s))
