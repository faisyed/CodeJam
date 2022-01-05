"""
Logic:
1) If character is alnum simply print out
2) if character is "(" push to stack
3) if character is ")" pop all items from stack until it is "("
4) if character is operator then push current char in stack if it has more precedence than top, else pop operators
until current char is greater than top of stack.
"""


def get_operator_precedence(op):
    if op == "+" or  op == "-":
        return 1
    elif op == "*" or op == "/" or op == "%":
        return 2
    elif op == "^":
        return 3
    else:
        return -1


def infix_to_postfix(exp):
    stack = []
    res = ""
    for ch in exp:
        if ch.isalnum():
            res += ch
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
        else:
            while stack and get_operator_precedence(stack[-1]) >= get_operator_precedence(ch):
                res += stack.pop()
            stack.append(ch)
    while stack:
        res += stack.pop()
    return res


if __name__ == "__main__":
    expr = input("Enter the infix expression to convert to postfix: ")
    post = infix_to_postfix(expr)
    print("Resultant postfix expression is: ", post)