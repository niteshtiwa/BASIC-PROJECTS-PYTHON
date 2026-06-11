# datetime:
# date :
# time :
# timedelta:
from datetime import datetime
from datetime import date 
from datetime import timedelta

now = datetime.now()
today = datetime.today().date()
specific_date = date(2023, 5, 17)
formatted_date = now.strftime("%Y-%m-%d %H:%M:%M")
today = datetime.today()
tomorrow = today +timedelta(days=1)
print(f"current date and time : {now}")
print(f"Today's date:{today}")
print(f"specific date: {specific_date}")
print(f"formated date and tme:{formatted_date}")
print(f" tomorrow date is {tomorrow}")
