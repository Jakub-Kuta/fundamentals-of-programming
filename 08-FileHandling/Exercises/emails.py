###
# Functions that fetch data from a raw email
#
import re

def read_email(file_name='email.txt'):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def find_address(header, file_name):
    email = read_email(file_name)
    match = re.search(r'^' + header + r':.*?([\w.+-]+@[\w-]+(?:\.[\w-]+)+)', email, re.MULTILINE)
    if match:
        return match.group(1)
    return ''

def email_sender(file_name='email.txt'):
    return find_address('From', file_name)

def email_recipient(file_name='email.txt'):
    return find_address('To', file_name)

def email_subject(file_name='email.txt'):
    email = read_email(file_name)
    match = re.search(r'^Subject:[ \t]*(.*)$', email, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ''

def email_body(file_name='email.txt'):
    email = read_email(file_name)
    match = re.search(r'\n[ \t]*\n(.*)', email, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ''
