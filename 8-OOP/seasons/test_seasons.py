from datetime import datetime
from seasons import Time
import seasons


def test_past_date(): ...


def test_sub():
    past_date = Time(datetime(2000, 1, 1))
    current_date = Time(datetime(2000, 1, 2))

    time_between = current_date - past_date

    assert time_between == "one thousand, four hundred and forty"
