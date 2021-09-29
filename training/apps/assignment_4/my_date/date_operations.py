from datetime import date, datetime, timedelta
from dateutil import relativedelta

def get_current_datetime() -> datetime:

    '''
        Returns current datetime
    '''

    return datetime.now()

def get_birth_date(age: str) -> date:
    
    '''
        Returns birth date from age as a string parameter
        entered in the format "x years, y months, z days"
    '''
    age_dict = {
        val.split(" ")[1]:val.split(" ")[0] 
        for val in age.split(", ")
    }

    birth_date = get_current_datetime() - timedelta(
        years=age_dict.get('years',0),
        months=age_dict.get('months',0),
        days=age_dict.get('days',0)
    )

    return birth_date.date()

def get_age_from_birth_date(birth_date: date) -> str:

    current_date = get_current_datetime().date()

    age = relativedelta.relativedelta(current_date, birth_date)

    return "{} years, {} months, {} days".format(age.years, age.months, age.days)

def time_to_50(birth_date: date) -> str:

    target_date = datetime.combine(birth_date, datetime.min.time()) + timedelta(years=50)

    current_date = get_current_datetime().date()

    expected = relativedelta.relativedelta(target_date, current_date)
    
    return "{} years, {} months, {} days".format(expected.years, expected.month, expected.days)



