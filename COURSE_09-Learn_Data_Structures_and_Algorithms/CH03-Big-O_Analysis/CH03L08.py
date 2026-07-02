def find_last_name(names_dict: dict[str, str], first_name: str) -> str | None:
    try:
        return names_dict[first_name]
    except KeyError:
        return None

