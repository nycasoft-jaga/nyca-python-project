import calendar
from datetime import datetime, timedelta

def generate_timetable(start_date, months):
    current_date = start_date
    timetable = []

    for _ in range(months):
        month_days = calendar.monthrange(current_date.year, current_date.month)[1]
        for day in range(1, month_days + 1):
            timetable.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)

    return timetable

# Start date for the timetable
start_date = datetime.now()

# Generate timetable for 6 months
timetable = generate_timetable(start_date, 6)

# Print the timetable
print("Timetable:")
for date in timetable:
    print(date)

# Print the calendar for all six months
for month_offset in range(6):
    year = (start_date.month + month_offset - 1) // 12 + start_date.year
    month = (start_date.month + month_offset - 1) % 12 + 1
    print(calendar.month(year, month))