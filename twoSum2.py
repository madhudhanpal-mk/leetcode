def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        curSum = numbers[l] + numbers[r]
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        elif curSum == target:
            return [l, r]
    return []

nums = [2,7,11,15]
t = 18

print(twoSum(nums,t))