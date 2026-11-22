###
# tv_show.py file
# main program
#
import tv

def main():
    # object creation
    tv_set = tv.TV()

    # object usage
    tv_set.show_status()
    tv_set.turn_on()
    tv_set.show_status()
    tv_set.turn_off()
    tv_set.show_status()

if __name__ == "__main__":
    main()
