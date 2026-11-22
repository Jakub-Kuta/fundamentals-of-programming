###
# Customer service in an office - queue of tickets
#
import queue

customers = queue.Queue()
ticket_number = 0

while True:
    print('1. New customer')
    print('2. Serve next customer')
    print('0. Quit')
    menu = input('Select an option: ')

    if menu == '1':
        ticket_number += 1
        customers.put(ticket_number)
        print(f'Your ticket number is {ticket_number}. Customers waiting: {customers.qsize()}')

    elif menu == '2':
        if not customers.empty():
            number = customers.get()
            print(f'Customer with ticket {number}, please come to the desk')
        else:
            print('No customers waiting')

    elif menu == '0':
        break
