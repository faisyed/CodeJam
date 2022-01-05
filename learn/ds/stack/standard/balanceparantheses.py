def check_balance(exp):
    stack = []
    flag = True
    for ch in exp:
        if ch in ["(", "{", "["]:
            stack.append(ch)
        else:
            if ch == ")" and stack[-1] == "(":
                stack.pop()
            elif ch == "}" and stack[-1] == "{":
                stack.pop()
            elif ch == "]" and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break
    if stack:
        flag = False
    return "Balanced" if flag else "Not Balanced"


if __name__ == "__main__":
    expr = input("Enter the parentheses expression: ")
    res =check_balance(expr)
    print(res)