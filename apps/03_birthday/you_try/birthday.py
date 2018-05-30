import datetime

def header():
    print('************************************')
    print('         Next Birthday')
    print('************************************')
    print()

def get_birthday_from_user():
    print('When where you born? ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday

def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date

    return dt.days 

def print_birthday_info(days):
    if days < 0:
        print('You had your birthday {} days ago.'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days.'.format(days))
    else:
        print('Ja, man har leva, ja man har leva......')

def main():
    header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_info(number_of_days)

main()