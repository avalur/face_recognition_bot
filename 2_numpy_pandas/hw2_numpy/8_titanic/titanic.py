import typing as tp


def male_age(df: tp.Any) -> float:
    """
    Return mean age of survived men, embarked in Southampton with fare > 30
    :param df: dataframe
    :return: mean age
    """


def nan_columns(df: tp.Any) -> tp.Any:
    """
    Return list of columns containing nans
    :param df: dataframe
    :return: series of columns
    """


def class_distribution(df: tp.Any) -> tp.Any:
    """
    Return Pclass distrubution
    :param df: dataframe
    :return: series with ratios
    """


def families_count(df: tp.Any, k: int) -> float:
    """
    Compute number of families with more than k members
    :param df: dataframe,
    :param k: number of members,
    :return: number of families
    """


def mean_price(df: tp.Any, tickets: tp.Any) -> float:
    """
    Return mean price for specific tickets list
    :param df: dataframe,
    :param tickest: list of tickets,
    :return: mean fare for this tickets
    """


def max_size_group(df: tp.Any, columns: tp.Any) -> tp.Any:
    """
    For given set of columns compute most common combination of values of these columns
    :param df: dataframe,
    :param columns: columns for grouping,
    :return: list of most common combination
    """


def dead_lucky(df: tp.Any) -> float:
    """
    Compute dead ratio of passengers with lucky tickets
    :param df: dataframe,
    :return: ratio of dead lucky passengers
    """
