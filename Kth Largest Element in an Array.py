import heapq

def findKthLargest(nums, k):
    maxHeap = [-x for x in nums]
    heapq.heapify(maxHeap)
    for i in range(k-1):
        heapq.heappop(maxHeap)

    return -maxHeap[0]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(findKthLargest(nums, k))