import collections


def topKFrequent(nums, k):
    c = collections.Counter(nums)
    return sorted(c, key=lambda x: c[x], reverse=True)[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))

#https://leetcode.com/problems/top-k-frequent-elements/description/
