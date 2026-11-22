###
# Calculates the total number of hours
#
winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}

total_hours = 0
for course, hours in winter_semester.items():
    total_hours += hours

print(f'The total number of hours in the winter semester is {total_hours}')
