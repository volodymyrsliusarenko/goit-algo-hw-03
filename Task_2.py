import random

def get_numbers_ticket(min, max, quantity):
    ticket = set()
    while len(ticket) < quantity:
        ticket.add(random.randint(min, max))
    ticket_numbers = list(ticket)
    ticket_numbers.sort()
    return ticket_numbers
    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
