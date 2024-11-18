def threeSum(nums):
    res = []
    nums.sort()

    l,r  = 0, len(nums) - 1

    for i,n in enumerate(nums):
        if n > 0 and n == nums[i] - 1:
            continue

        curSum = n + nums[l] + nums[r]
        if curSum > 0:
            r -= 1
        elif curSum < 0:
            l += 1
        else:
            res.append ([n, nums[l], nums[r]])
            l += 1
            while nums[l] == nums[l - 1] and l < r:
                l+=1
    return res


nums = [-2,1,5,-3,-1,-7,5,3,-1,-2,0,-1,-2,-3,0,0]
print(threeSum(nums))
