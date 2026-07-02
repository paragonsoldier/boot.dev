def count_names(list_of_lists: list[list[str]], target_name: str) -> int:
    count = 0
    for list in list_of_lists:
        for name in list:
            if name == target_name:
                count += 1
    return count

