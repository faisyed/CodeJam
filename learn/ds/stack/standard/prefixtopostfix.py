def prefix_to_postfix(exp):
    rev_exp = exp[::-1]
    stack = []
    for ch in rev_exp:
        if ch.isalnum():
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            re = op1 + op2 + ch
            stack.append(re)
    return stack.pop()


if __name__ == "__main__":
    expr = input("Enter prefix expression to convert to postfix: ")
    res = prefix_to_postfix(expr)
    print("Resultant postfix expression:", res)