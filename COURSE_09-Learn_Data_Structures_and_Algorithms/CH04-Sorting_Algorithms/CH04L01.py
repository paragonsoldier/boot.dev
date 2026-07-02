class Influencer:
    def __init__(self, num_selfies: int, num_bio_links: int) -> None:
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self) -> str:
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer: Influencer) -> int:
    return influencer.num_bio_links * 5 + influencer.num_selfies


def vanity_sort(influencers: list[Influencer]) -> list[Influencer]:
    for influencer in influencers:
        influencer.vanity = vanity(influencer)
    return sorted(influencers, key=vanity)

