###
# Fetches and prints data from a raw email
#
import emails

print('Sender:', emails.email_sender())
print('Recipient:', emails.email_recipient())
print('Subject:', emails.email_subject())
print('Body:')
print(emails.email_body())
