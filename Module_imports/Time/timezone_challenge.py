import datetime
import pytz

MENU = """tz + country_timezone_code : Shows time in country with timezone\
country_timezone_code
tzs : Shows all timezones
menu : Shows menu
c + country_name : Searches for countries with substring country_name
exit : Exits application
"""


def print_timeones():
    ''' prints all timezones in pytz
    '''
    for x in sorted(pytz.country_names):
        print(x, ":", pytz.country_names[x])


choice = "menu"
while choice != "exit":
    if "tzs" in choice:
        print_timeones()
    elif "c" in choice:
        country = choice.split()[1]
        for c in pytz.country_names:
            name = pytz.country_names[c]
            if country.lower() in name.lower():
                print(f"{name}'s timezone is {c}")
    elif "tz" in choice:
        timezone_name = pytz.country_timezones[choice.split()[1]][0]
        timezone_zone = pytz.timezone(timezone_name)
        timezone_time = datetime.datetime.now(tz=timezone_zone)  # type: ignore
        print(f"{timezone_name}'s time is {timezone_time}")
    elif "menu" in choice:
        print(MENU)
    else:
        print("Choice is invalid")
        print(MENU)
    choice = input("enter your choice:  ")
