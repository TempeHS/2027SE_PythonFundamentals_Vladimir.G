from datetime import datetime

import sys
import inflect

p = inflect.engine()


class Time:

    @classmethod
    def get(cls):

        date_past = input("Date:")

        try:
            date_past = datetime.strptime(date_past, "%Y/%m/%d")
            return cls(date_past)
        except ValueError:
            sys.exit("Invalid Date")

    def __init__(self, date):
        self.date = date.replace(hour=0, minute=0, second=0, microsecond=0)

    def __sub__(self, other):
        time_between = self.date - other.date
        minutes = int(time_between.total_seconds() // 60)
        return p.number_to_words(minutes)


def main():
    date_past = Time.get()
    date_today = Time(datetime.today())

    print(f"Time between dates: {date_today - date_past}")


if __name__ == "__main__":
    main()
