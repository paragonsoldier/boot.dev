def area_sum(rectangles):
    sum_areas = 0
    for rect in rectangles:
        area = rect["height"] * rect["width"]
        sum_areas += area
    return sum_areas

