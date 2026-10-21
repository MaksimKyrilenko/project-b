from datetime import date
from src.date_utils import format_date, days_between, add_days
from src.string_utils import reverse_string, capitalize_words, truncate, slugify


def test_format_date():
    assert format_date(date(2026, 10, 21)) == '21.10.2026'


def test_format_date_weekday():
    # 21.10.2026 — среда (ср)
    assert format_date(date(2026, 10, 21), weekday=True) == '21.10.2026 (ср)'


def test_days_between():
    assert days_between(date(2026, 10, 1), date(2026, 10, 21)) == 20


def test_add_days():
    assert add_days(date(2026, 10, 21), 10) == date(2026, 10, 31)


def test_reverse_string():
    assert reverse_string('abc') == 'cba'


def test_capitalize_words():
    assert capitalize_words('hello world') == 'Hello World'


def test_truncate_short():
    assert truncate('hi', 10) == 'hi'


def test_truncate_long():
    result = truncate('Привет, мир! Это длинная строка', 15)
    assert result.endswith('…')
    assert len(result) == 15


def test_slugify():
    assert slugify('Hello World') == 'hello-world'
