from datetime import datetime
import pytz

# Create timezone-aware datetime
utc = pytz.utc
now_utc = datetime.now(utc)


eastern = pytz.timezone('US/Eastern')
dt = datetime(2024, 11, 3, 1, 30)
dt_eastern = eastern.localize(dt, is_dst=None)


dt1 = datetime(2024, 7, 1, 12, 0, 0, tzinfo=pytz.UTC)
dt2 = datetime(2024, 7, 1, 8, 0, 0, tzinfo=pytz.timezone('US/Eastern'))


dt = datetime.strptime("2024-07-01 14:30:00", "%Y-%m-%d %H:%M:%S")
formatted_date = dt.strftime("%B %d, %Y")


from datetime import timedelta
future_date = datetime.now() + timedelta(days=10)
