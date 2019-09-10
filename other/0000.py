T = int(input())

dots = [] 
regions = []
for i in range(T):
    regions.append([])
    dots.append([])
    _, m  = (int(digit) for digit in input().split())
    dots[i] = [int(digit) for digit in input().split()]
    for _ in range(m):
        regions[i].append([int(digit) for digit in input().split()])


for i in range(T):
    print('Case #{}'.format(i+1))
    # print(dots, regions)
    for region in regions[i]:
        l, r = region
        if r < l:
            l, r = r, l
        dots[i].sort()
        k = 0
        j = len(dots[i]) - 1
        if dots[i][k] > r or dots[i][j] < l:
            res = 0
        else:
            while dots[i][k] < l:
                k += 1
            while dots[i][j] > r:
                j -= 1 
            res = j - k + 1       
        print('{}'.format(res))



2
10 5
0 1 2 3 4 5 6 7 8 9 
0 5  
10 20
-5 -3
7 7
100 105
5 1
1 1 1 1 1
0 2
