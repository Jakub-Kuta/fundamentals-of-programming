###
# Statistics class
#
class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self):
        number = int(input('Enter number: '))
        self.numbers.append(number)

    def show_numbers(self):
        for number in self.numbers:
            print(number, end=' ')
        print()

    def maximum(self):
        largest = self.numbers[0]
        for number in self.numbers:
            if number > largest:
                largest = number
        return largest

    def minimum(self):
        smallest = self.numbers[0]
        for number in self.numbers:
            if number < smallest:
                smallest = number
        return smallest

    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        ordered = sorted(self.numbers)
        n = len(ordered)
        if n % 2 == 1:
            return ordered[n // 2]
        return (ordered[n // 2 - 1] + ordered[n // 2]) / 2

    def print_statistics(self):
        print('Numbers:', end=' ')
        self.show_numbers()
        print('Minimum:', self.minimum())
        print('Maximum:', self.maximum())
        print('Arithmetic mean:', self.mean())
        print('Median:', self.median())

stats = Statistics()
for i in range(5):
    stats.add_number()
stats.print_statistics()
