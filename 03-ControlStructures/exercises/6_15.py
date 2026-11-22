###
# EAN-13 check: exactly 13 digits; 590 at the start = made in Poland.
#
ean = input('Enter EAN-13 article number: ')

if len(ean) == 13 and ean.isdigit():
    print('Article number is correct')
    if ean[0:3] == '590':
        print('Article manufactured in Poland')
else:
    print('Article number is incorrect')
