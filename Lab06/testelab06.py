c = [[1,2],[2,3],[3,4]]
a = [[c[i][j] for i in range(len(c))] for j in range(len(c[0]))]
print(a)