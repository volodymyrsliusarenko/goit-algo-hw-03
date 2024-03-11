import random

def get_numbers_ticket(min, max, quantity):
    ticket = set()
    while len(ticket) < quantity:
        if min < max and quantity <= (max - min):
            ticket.add(random.randint(min, max))
            ticket_numbers = list(ticket)
            ticket_numbers.sort()
        else:
            ticket_numbers = []
            break      
    return ticket_numbers
    
lottery_numbers = get_numbers_ticket(7, 15, 9)
print("Ваші лотерейні числа:", lottery_numbers)
