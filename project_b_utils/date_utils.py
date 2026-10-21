from datetime import date, timedelta

WEEKDAYS = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']


def get_current_date():
    return date.today()


def format_date(value, fmt='%d.%m.%Y', weekday=False):
    result = value.strftime(fmt)
    return f'{result} ({WEEKDAYS[value.weekday()]})' if weekday else result


def days_between(start, end):
    return abs((end - start).days)


def add_days(value, days):
    return value + timedelta(days=days)
