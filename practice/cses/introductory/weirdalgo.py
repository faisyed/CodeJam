def weird_algo(num):
    ls = list()
    ls.append(num)
    while num != 1:
        if num % 2 == 0:
            num //= 2
            ls.append(num)
        else:
            num *= 3
            num += 1
            ls.append(num)
    return ls


if __name__=="__main__":
    n = int(input())
    res = weird_algo(n)
    for val in res:
        print(val,end=" ")