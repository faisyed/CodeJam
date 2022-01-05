def prefix_to_infix(exp):
    rev_exp = exp[::-1]
    stack = []
    for ch in rev_exp:
        if ch.isalnum():
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            re = "(" + op1 + ch + op2 + ")"
            stack.append(re)
    return stack.pop()


if __name__ == "__main__":
    expr = input("Enter the prefix expression to convert to infix: ")
    res = prefix_to_infix(expr)
    print("Resultant infix expression:", res)
