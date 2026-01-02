def avg_luck_boost(luck_boosts):
    if luck_boosts == []:
        return 0.0
    total = 0
    for boost in luck_boosts:
        total += boost
    return total / len(luck_boosts)

