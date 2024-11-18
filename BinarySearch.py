def binarySearch(nums, item):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        mid_value = nums[mid]
        if mid_value == item:
            return mid
        elif item > mid_value:
            l += 1
        else:
            r -= 1
    return -1

n = [2,4,6,7,9,45,56,78]
i = 45

print(binarySearch(n,i))
        
