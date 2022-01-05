def postfix_to_infix(exp):
    stack = []
    for ch in exp:
        if ch.isalnum():
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            re = "(" + op1 + ch + op2 + ")"
            stack.append(re)
    return stack.pop()


if __name__ == "__main__":
    expr = input("Enter the postfix expression to convert to infix: ")
    res = postfix_to_infix(expr)
    print("Resultant infix expression:", res)