def remove_nonints(nums):
    new_nums = []
    for num in nums:
        if type(num) == int:
            new_nums.append(num)
    return new_nums
