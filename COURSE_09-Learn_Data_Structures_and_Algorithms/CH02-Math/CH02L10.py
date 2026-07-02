import math

def log_scale(data: list[float], base: float) -> list[float]:
    logs = []
    for num in data:
        logs.append(math.log(num, base))
    return logs
        

