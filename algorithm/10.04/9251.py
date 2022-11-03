def LCS(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m] == Y[n]:
        return 1 + lcs[n-1][m-1]
    else:
        return max(lcs[n-1][m], lcs[n][m-1])


X = list(input())
X.insert(0, 0)
Y = list(input())
Y.insert(0, 0)

lcs = [[0 for j in range(len(X))] for i in range(len(Y))]

for n in range(1, len(Y)):
    for m in range(1, len(X)):
        lcs[n][m] = LCS(X, Y, m, n)

print(lcs[len(Y) - 1][len(X) - 1])
