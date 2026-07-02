def find_minimum(nums: list[int]) -> float | None:
    minimum = float("inf")
    if len(nums) == 0: 
        return None
    for num in nums: 
        if num < minimum: 
            minimum = num
    return minimum

