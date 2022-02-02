def go():
  dates_and_repeats = []
  for year in range(2000, 3000):
    for month in range(1, 13):
      for day in range(1, get_days(month, year)+1):
        date_str = f"{pad(month)}/{pad(day)}/{year}"
        dates_and_repeats.append((date_str, get_max_repeats(date_str)))
  
  dates_and_repeats = sorted(dates_and_repeats, key=lambda x: x[1], reverse=True)
  return dates_and_repeats

def get_max_repeats(date_str):
  max_repeats = 0
  for x in range(0, 10):
    max_repeats = max(date_str.count(str(x)), max_repeats)
  return max_repeats

def pad(num):
  snum = str(num)
  if len(snum) == 1:
    return f"0{snum}"
  return snum

def get_days(month, year):
  days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    return 29
  else:
    return days[month-1]