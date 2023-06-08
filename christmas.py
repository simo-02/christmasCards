import os

with open('employees.txt', 'r') as my_file:
    recipients = my_file.read().splitlines()

with open('template.txt', 'r') as my_file:
    template = my_file.read()

if not os.path.exists('christmasCards'):
    os.mkdir('christmasCards')

for recipient in recipients:
    
    card = template.replace('NAME', recipient)
    card_file = f'christmasCards/{recipient}.txt'
    with open(card_file, mode='w') as my_file:
        my_file.write(card)

    print(f'Christmas card created for: {recipient}.')



