# import time

# print("The epoch on this system starts at" +
#       time.strftime("%c", time.gmtime(0)))

# print(
#     f"The current timezone is {time.tzname[0]} \
# with an offset of {time.timezone}")

# if time.daylight != 0:
#     print("\tDaylight Saving Time is in effect in this location")
#     print("\tThe DST timezone is " + time.tzname[1])

# print("Local time is", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print("UTC time is", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

import datetime
import pytz

# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print(f"The time in {country} is {local_time}")
print(f"UTC is {datetime.datetime.utcnow()}")

for x in pytz.all_timezones:
    print(x)

for x in sorted(pytz.country_names):
    print(x, ":", pytz.country_names[x])

print(pytz.country_names)

for x in sorted(pytz.country_names):
    # print(f"{x}: {pytz.country_names[x]}, {pytz.country_timezones[x]}")
    # Code above gives error because some countries don't have timezone
    # print(f"{x}: {pytz.country_names[x]}, {pytz.country_timezones.get(x)}")
    # Line above fixes problem but code below is more elegant
    print(x, ":", pytz.country_names[x])
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print(f"\t{zone}: {local_time}")
    else:
        print("\t\tNo time zone defined")
