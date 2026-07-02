def get_follower_prediction(
    follower_count: int, influencer_type: str, num_months: int
) -> int:
    if influencer_type == "fitness":
        r = 4
    elif influencer_type == "cosmetic":
        r = 3
    else:
        r = 2
    
    return follower_count * r ** num_months

