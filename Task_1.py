from datetime import datetime

date = input('Please enter date YYYY-MM-DD: ')

def get_days_from_today(date):
    current_date = datetime.today()
    try:
        date_formated = datetime.strptime(date, "%Y-%m-%d")
        print(current_date.toordinal() - date_formated.toordinal())
    except ValueError:
        print('Incorrect data format, please try again')

get_days_from_today(date)

