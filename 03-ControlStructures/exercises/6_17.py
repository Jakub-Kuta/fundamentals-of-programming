###
# Converts time from 24-hour format (hh:mm) to 12-hour format.
#
time = input('Enter time (24-hour format): ')
parts = time.split(':')
hour = int(parts[0])
minutes = parts[1]

if hour == 0:
    print(f'Time in 12-hour format: 12:{minutes}am')
elif hour < 12:
    print(f'Time in 12-hour format: {hour}:{minutes}am')
elif hour == 12:
    print(f'Time in 12-hour format: 12:{minutes}pm')
else:
    print(f'Time in 12-hour format: {hour - 12}:{minutes}pm')
