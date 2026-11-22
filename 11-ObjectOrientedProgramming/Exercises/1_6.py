###
# Class describing a smartphone
#
class Phone():
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
        self.is_locked = True

    def unlock(self):
        self.is_locked = False
        print('Phone unlocked')

    def lock(self):
        self.is_locked = True
        print('Phone locked')

    def charge(self, percent):
        self.battery_level = min(100, self.battery_level + percent)
        print(f'Phone charged, battery: {self.battery_level}%')

    def make_call(self, contact):
        if self.is_locked:
            print('Unlock the phone first')
        else:
            self.battery_level -= 1
            print(f'Calling {contact}...')

phone = Phone('Apple', 'iPhone 17 Pro', 60)

phone.make_call('Anna')
phone.unlock()
phone.make_call('Anna')
phone.charge(30)
phone.lock()

print('Brand:', phone.brand)
print('Model:', phone.model)
print('Battery level:', phone.battery_level)
print('Locked:', phone.is_locked)
