def sort_dates(dates):
  dates_copy = dates.copy()
  dates_copy = list(map(lambda x: x.split("-"), dates_copy))
  dates_copy = sorted(dates_copy, key=lambda x: x[2]+x[0]+x[1]) # Sort by MONTH-DAY-YEAR
  dates_copy = list(map(lambda x: "-".join(x), dates_copy))
  return dates_copy
