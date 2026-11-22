import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'170cm is {converters.cm_to_inches(170):.2f} inches')
print(f'5 feet 11 inches is {converters.feet_inches_to_cm(5, 11):.2f}cm')
