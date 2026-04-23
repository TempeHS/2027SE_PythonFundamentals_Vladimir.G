from datetime import datetime
from seasons import Time
import seasons


def test_sub():
    past_date = Time(datetime(2000, 1, 1))
    current_date = Time(datetime(2000, 1, 2))

    time_between = current_date - past_date

    assert time_between == "one thousand, four hundred and forty"

    past_date_1 = Time(datetime(1999, 1, 1))
    current_date_1 = Time(datetime(2000, 1, 1))

    time_between_1 = current_date_1 - past_date_1

    assert time_between_1 == "five hundred and twenty-five thousand, six hundred"
