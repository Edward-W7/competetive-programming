n = int(input())
height = [int(i) for i in input().split()]
q = int(input())

for x in range(q):
    quer = [int(i) for i in input().split()]
    ans = 0
    if len(quer) == 5:
        i, j, a, b = quer[1], quer[2], quer[3], quer[4]
        for x in height[i:j+1]:

            if a <= x and x <= b:
                ans += 1
        print(ans)
    else:
        height[quer[1]] = quer[2]
