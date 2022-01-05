def permutations(num):
    ls = []
    if num == 4:
        return [2,4,1,3]
    for i in range(1, num+1, 2):
        ls.append(i)
    for i in range(2, num+1, 2):
        ls.append(i)
    return ls


if __name__ == "__main__":
    n = int(input())
    res = permutations(n)
    if n in [2,3]:
        print("NO SOLUTION")
    else:
        for val in res:
            print(val,end=" ")
