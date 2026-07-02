def average_followers(nums: list[int]) -> float | None:
    if len(nums) == 0:
        return None
    return sum(nums) / len(nums)

