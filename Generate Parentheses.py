def generateParenthesis(n):
    result = []

    def backtrack(open, close, stack):
        if open == close == n:
            return result.append("".join(stack))
        if open < n:
            stack.append("(")
            backtrack(open + 1, close, stack)
            stack.pop()
        if open > close:
            stack.append(")")
            backtrack(open, close + 1, stack)
            stack.pop()

    backtrack(0, 0, [])
    return result


n = 3
print(generateParenthesis(n))
