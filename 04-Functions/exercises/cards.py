###
# Module with a function that masks a credit card number
#
def hide(card_number):
    hidden_digits = len(card_number) - 6
    return card_number[0:2] + '*' * hidden_digits + card_number[-4:]
