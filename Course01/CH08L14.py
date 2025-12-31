def calculate_experience_points(level):
    xp = 0
    for i in range(level):
        xp += i * 5
    return xp
