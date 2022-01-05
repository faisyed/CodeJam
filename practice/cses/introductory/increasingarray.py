def increase_array(n, ls):
    cnt = 0
    for i in range(1, n):
        if ls[i] >= ls[i-1]:
            continue
        else:
            diff = abs(ls[i]-ls[i-1])
            cnt += diff
            ls[i] += diff
    return cnt


if __name__ == "__main__":
    n = int(input())
    ls = list(map(int, input().split()))
    res = increase_array(n, ls)
    print(res)
