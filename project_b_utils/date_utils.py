from datetime import date, datetime, timedelta


def get_current_date(as_datetime=False):
    return datetime.now() if as_datetime else date.today()


def format_date(value, fmt='%d.%m.%Y'):
    return value.strftime(fmt)


def days_between(start, end):
    return abs((end - start).days)


def add_days(value, days):
    return value + timedelta(days=days)
