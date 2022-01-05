"""
Logic:
1) reverse expression
2) apply postfix but remember "(" becomes ")" and vice versa
3) reverse final string
"""


def precedence(op):
    if op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/" or op == "%":
        return 2
    elif op == "^":
        return 3
    else:
        return -1


def infix_to_prefix(exp):
    rev_exp = exp[::-1]
    stack = []
    res = ""
    for ch in rev_exp:
        if ch.isalnum():
            res += ch
        elif ch == ")":
            stack.append(ch)
        elif ch == "(":
            while stack[-1] != ")":
                res += stack.pop()
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                res += stack.pop()
            stack.append(ch)
    while stack:
        res += stack.pop()
    return res[::-1]


if __name__ == "__main__":
    expr = input("Enter the infix to convert to prefix: ")
    pre = infix_to_prefix(expr)
    print("Resultant prefix expression is:", pre)