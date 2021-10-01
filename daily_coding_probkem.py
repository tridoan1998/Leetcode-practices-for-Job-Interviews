def two_sum( nums, k):
    if len(nums) <= 1:
        return -1
    else:
        hm = {}
        for i in range(len(nums)):
            if nums[i] not in hm.values():
                hm[i] = nums[i]
           # else:
            #    hm[i] += 1
        temp = 0
        for i in range(len(nums)):
            temp = k - nums[i]
            print(temp)
            if temp == hm.values():
                return [i, hm.keys(temp)]
        return hm



nums = [2, 7, 11, 15]
k = 9
print(two_sum(nums, k))