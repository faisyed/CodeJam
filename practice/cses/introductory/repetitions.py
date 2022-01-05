def repetitions(s):
    mx = 1
    prev = s[0]
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == prev:
            cnt += 1
        else:
            if mx<cnt:
                mx = cnt
            prev = s[i]
            cnt = 1
    if mx<cnt:
        mx = cnt
    return mx


if __name__=="__main__":
    s = input()
    res = repetitions(s)
    print(res)
