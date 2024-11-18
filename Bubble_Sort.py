def bubleSOrt(nums):
    length = len(nums) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(length):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    
    return nums


nums = [2,5,7,4,2,9,0,1,23,6,45,4]
print(bubleSOrt(nums))