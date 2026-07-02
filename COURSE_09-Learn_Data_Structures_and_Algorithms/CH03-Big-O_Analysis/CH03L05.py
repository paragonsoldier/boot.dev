def get_avg_brand_followers(all_handles: list[list[str]], brand_name: str) -> float:
    count = 0
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                count += 1
    return count / len(all_handles)

