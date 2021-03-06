""" CSC110 Final Project

This file is Copyright (c) 2021 Edward Han, Zekun Liu, Arvin Gingoyon
"""
import csv
import datetime
from tweet import Tweet


def read_tweet_data(filename: str) -> list[Tweet]:
    """ Read csv file data and create Tweet dataclasses using the values in each column

    Preconditions:
        - the file has to have the following headers: id,date,content
    """

    inputs_so_far = []

    with open(filename, encoding='utf8') as file:
        reader = csv.reader(file, delimiter=',')
        # Skip the header because it is not useful
        next(reader)

        for row in reader:
            tweet_id = int(row[0])
            raw_date = row[1]
            content = row[2]

            # Convert every line into a Tweet object
            tweet = Tweet(tweet_id, parse_time(raw_date), content)
            inputs_so_far.append(tweet)

    return inputs_so_far


def parse_time(raw_time: str) -> datetime.datetime:
    """Take a raw unparsed date and time string from the CSV file as input and return a
    datetime.datetime object

    >>> import datetime
    >>> parse_time('2021-12-10 01:40:48+00:00')
    datetime.datetime(2021, 12, 10, 1, 40)
    """

    date_and_time = raw_time.split(' ')
    split_date = [int(value) for value in date_and_time[0].split('-')]
    split_time = list(date_and_time[1].split(':'))
    parsed_data = datetime.datetime(day=split_date[2], month=split_date[1],
                                    year=split_date[0], hour=int(split_time[0]),
                                    minute=int(split_time[1]))

    return parsed_data


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    python_ta.check_all(config={
        'extra-imports': ['csv', 'datetime', 'tweet'],
        'allowed-io': ['read_tweet_data'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
