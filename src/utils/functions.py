import datetime

def date_1M(date: datetime.date):
    assert isinstance(date, datetime.date)
    return date - datetime.timedelta(days=30)

def date_1Y(date: datetime.date):
    assert isinstance(date, datetime.date)
    return date - datetime.timedelta(days=365)

def date_Ytd(date: datetime.date):
    assert isinstance(date, datetime.date)
    return datetime.date(date.year, 1, 1)