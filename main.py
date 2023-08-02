n = int(input())
a = list(map(int, __import__("sys").stdin.readline().strip().split()))

moves = 0
a.sort()
for i, j in zip(range(1, len(a) + 1), a):
    moves += abs(j - i)

print(moves)
