from datetime import datetime

date = input('Please enter date YYYY-MM-DD: ')

def get_days_from_today(date):
    current_date = datetime.today()
    days_differnce = 0
    try:
        date_formated = datetime.strptime(date, "%Y-%m-%d")
        days_differnce = current_date.toordinal() - date_formated.toordinal()
    except ValueError:
        print('Incorrect data format, please try again')
        days_differnce = None
    return days_differnce

print(get_days_from_today(date))

