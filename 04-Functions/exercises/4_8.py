###
# Returns the time as a string in the 24-hour or 12-hour format
#
def time_string(hours, minutes, time_format):
    result = ''
    if time_format == '24':
        result = f'{hours:02d}:{minutes:02d}'
    else:
        suffix = 'am'
        hour12 = hours
        if hours == 0:
            hour12 = 12
        elif hours == 12:
            suffix = 'pm'
        elif hours > 12:
            hour12 = hours - 12
            suffix = 'pm'
        result = f'{hour12}:{minutes:02d}{suffix}'
    return result

print("time_string(15, 38, '24') returns", time_string(15, 38, '24'))
print("time_string(8, 3, '24') returns", time_string(8, 3, '24'))
print("time_string(0, 5, '24') returns", time_string(0, 5, '24'))
print("time_string(11, 15, '12') returns", time_string(11, 15, '12'))
print("time_string(0, 7, '12') returns", time_string(0, 7, '12'))
print("time_string(7, 30, '12') returns", time_string(7, 30, '12'))
print("time_string(12, 46, '12') returns", time_string(12, 46, '12'))
print("time_string(13, 10, '12') returns", time_string(13, 10, '12'))
print("time_string(19, 2, '12') returns", time_string(19, 2, '12'))
