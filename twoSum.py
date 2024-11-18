def twoSum(nums, target):
    hashMap = {}

    for i,n in enumerate(nums):
        curSum = target - n

        if curSum in hashMap:
            print(hashMap[curSum], i)
        else:
            hashMap[n] = i
    return []



n = [2,4,7,9]
tar = 6

print(twoSum(n,tar))