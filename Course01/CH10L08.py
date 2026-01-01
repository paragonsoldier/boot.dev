def get_most_common_enemy(enemies_dict):
    most_common_enemy = None
    max_so_far = float("-inf")
    for enemy in enemies_dict:
        count = enemies_dict[enemy]
        if count > max_so_far:
            max_so_far = count
            most_common_enemy = enemy
    return most_common_enemy
