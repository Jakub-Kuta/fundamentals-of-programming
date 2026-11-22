###
# f(dice) returns the number rolled the most times in a row
#
def f(dice):
    best_digit = dice[0]
    best_length = 1
    length = 1
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            length += 1
        else:
            length = 1
        if length > best_length:
            best_length = length
            best_digit = dice[i]
    return int(best_digit)

if __name__ == "__main__":
    print('f("5233165554211") returns', f("5233165554211"))
    print('f("2133") returns', f("2133"))
