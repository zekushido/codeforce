n = int(input())
a = list(map(int, input().split()))

l = 0
r = n - 1

sid = 0
dim = 0
turn = 0

while l <= r:
    if a[l] > a[r]:
        c = a[l]
        l += 1
    else:
        c = a[r]
        r -= 1

    if turn == 0:
        sid += c
    else:
        dim += c

    turn = 1 - turn  # switch turn

print(sid, dim)