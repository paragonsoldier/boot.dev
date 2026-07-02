def find_max(nums: list[float]) -> float:
    max = float("-inf")
    for num in nums: 
        if num > max: 
            max = num
    return max

