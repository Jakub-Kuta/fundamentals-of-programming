###
# Payment card PIN check: up to three attempts, then the card is blocked.
#
correct_pin = '0805'
attempts = 0

while attempts < 3:
    pin = input('Enter the PIN code: ')
    if pin == correct_pin:
        print('PIN correct')
        break
    print('Incorrect...')
    attempts += 1

if attempts == 3:
    print('Sorry, your payment card has been blocked.')
