def topKFrequent(nums, k):
    my_dict = {}
    for i in nums:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    return sorted(my_dict.keys(),key = lambda x:my_dict[x],reverse=True)[:k]

nums = [4,1,-1,2,-1,2,3]
k = 2
topKFrequent(nums, k)