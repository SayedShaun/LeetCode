def findCenter(edges):
    hashSet = set()
    for i, j in edges:
        if i in hashSet:
            return i
        if j in hashSet:
            return j
        hashSet.add(i)
        hashSet.add(j)

edges = [[1,2],[2,3],[4,2]]
print(findCenter(edges))