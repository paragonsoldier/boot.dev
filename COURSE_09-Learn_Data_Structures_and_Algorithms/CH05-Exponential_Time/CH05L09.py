def exponential_growth(n: int, factor: int, days: int) -> list[int]:
    growth = [n]
    for i in range(days):
        n = n * factor
        growth.append(n)
    return growth


