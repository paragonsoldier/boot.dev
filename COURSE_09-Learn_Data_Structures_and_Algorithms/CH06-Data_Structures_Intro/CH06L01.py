def count_marketers(job_titles: list[str]) -> int:
    count = 0
    for title in job_titles:
        if title.lower() == "marketer":
            count += 1
    return count

