import datetime

users = [
    {"name": "John Doe", "birthday": "1985.03.19"},
    {"name": "Jane Smith", "birthday": "1990.03.11"},
    {"name": "Jane Smith2", "birthday": "1990.03.14"},
    {"name": "Jane Smith3", "birthday": "1990.03.17"}
    
]

def get_upcoming_birthdays(users):
    today = datetime.date.today()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.datetime.strptime(user['birthday'], "%Y.%m.%d").date() # змінюємо на datetime

        birthday_this_year = datetime.date(today.year, birthday.month, birthday.day) # отримуємо всі дн цього року
        
        if birthday_this_year < today:
            birthday_this_year = datetime.date(today.year + 1, birthday.month, birthday.day) # якщо дата дн вже пройшла, переносимо на наступний рік

        delta = birthday_this_year - today # знаходимо різницю між датою дн і поточною датою

        if delta.days <= 7: # первіряємо лише майбутні 7 днів
            if birthday_this_year.weekday() >= 5:
                if birthday_this_year.weekday() == 5: # якщо субота, переносимо на понеділок
                    birthday_this_year += datetime.timedelta(days=2)
                else:
                    birthday_this_year += datetime.timedelta(days=1) # якщо неділя, переносимо на понеділок
            
            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')  # Форматуємо дату у рядок
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str}) # додаємо у список

    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)