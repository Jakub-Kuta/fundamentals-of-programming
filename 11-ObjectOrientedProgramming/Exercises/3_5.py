###
# TV class: the status shows the name of the channel
#
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        print('Channel list:')
        for i in range(len(self.channels)):
            print(f'{i + 1}. {self.channels[i]}')

    def show_status(self):
        if self.is_on:
            if self.channel_no >= 1 and self.channel_no <= len(self.channels):
                name = self.channels[self.channel_no - 1]
                print(f'TV is on, channel {self.channel_no} ({name})')
            else:
                print(f'TV is on, channel {self.channel_no}')
        else:
            print('TV is off')

def main():
    tv_set = TV()
    tv_set.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery', 'HBO'])
    tv_set.show_status()
    tv_set.turn_on()
    tv_set.show_status()
    tv_set.set_channel(4)
    tv_set.show_status()
    tv_set.set_channel(7)
    tv_set.show_status()
    tv_set.set_channel(9)
    tv_set.show_status()
    tv_set.set_channel(2)
    tv_set.show_status()
    tv_set.turn_off()
    tv_set.show_status()

if __name__ == "__main__":
    main()
