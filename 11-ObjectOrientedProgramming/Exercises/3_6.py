###
# TV class with volume adjustment in the range 0-10
#
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

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

    def volume_up(self):
        if self.volume < 10:
            self.volume += 1

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1

    def show_status(self):
        if self.is_on:
            if self.channel_no >= 1 and self.channel_no <= len(self.channels):
                name = self.channels[self.channel_no - 1]
                print(f'TV is on, channel {self.channel_no} ({name}), volume {self.volume}')
            else:
                print(f'TV is on, channel {self.channel_no}, volume {self.volume}')
        else:
            print('TV is off')

def main():
    tv_set = TV()
    tv_set.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery', 'HBO'])
    tv_set.turn_on()
    tv_set.show_status()
    for i in range(12):
        tv_set.volume_up()
    tv_set.show_status()
    for i in range(4):
        tv_set.volume_down()
    tv_set.show_status()
    for i in range(10):
        tv_set.volume_down()
    tv_set.show_status()
    tv_set.turn_off()
    tv_set.show_status()

if __name__ == "__main__":
    main()
