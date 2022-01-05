def postfix_to_prefix(exp):
    stack = []
    for ch in exp:
        if ch.isalnum():
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            re = ch + op1 + op2
            stack.append(re)
    return stack.pop()


if __name__ == "__main__":
    expr = input("Enter postfix to convert to prefix: ")
    res = postfix_to_prefix(expr)
    print("Resultant prefix expression:", res)