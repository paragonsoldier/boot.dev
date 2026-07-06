def last_work_experience(work_experiences: list[str]) -> str | None:
    if work_experiences == []:
        return None
    return work_experiences[-1]

