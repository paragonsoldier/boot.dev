def format_line(line):
    stripped = line.strip()
    capitalized = stripped.upper()
    rm_periods = capitalized.replace('.', '')
    suffixed = f"{rm_periods}..."
    return suffixed

