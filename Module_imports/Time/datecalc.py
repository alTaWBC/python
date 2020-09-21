from time import process_time as timer3
from time import monotonic as timer2
from time import perf_counter as timer1
from time import time as timer
import random
import time

# # print(time.gmtime(0))
# # print()
# # print(time.localtime(time.time()))
# # print()
# # print(time.localtime())
# # print()
# # print(time.time())

# time_here = time.localtime()
# print(time_here)
# print(f"Year: {time_here[0]} or {time_here.tm_year}")
# print(f"Month: {time_here[1]} or {time_here.tm_mon}")
# print(f"Day: {time_here[2]} or {time_here.tm_mday}")

# Simple timer

input("Press enter to start")

wait_time = random.randint(1, 3)
time.sleep(wait_time)
start_time = timer()
input("Press enter to stop")

end_time = timer()

print(f"Start: {time.strftime('%X', time.localtime(start_time))}")
print(f"End: {time.strftime('%X', time.localtime(end_time))}")
# We can see options in time library

print(f"Your reaction time was {end_time-start_time} seconds!")

# A more precise clock with times different from localtime

input("Press enter to start")

wait_time = random.randint(1, 3)
time.sleep(wait_time)
start_time = timer1()
input("Press enter to stop")

end_time = timer1()

print(f"Start: {time.strftime('%X', time.localtime(start_time))}")
print(f"End: {time.strftime('%X', time.localtime(end_time))}")
# We can see options in time library

print(f"Your reaction time was {end_time-start_time} seconds!")


# Another counter

input("Press enter to start")

wait_time = random.randint(1, 3)
time.sleep(wait_time)
start_time = timer2()
input("Press enter to stop")

end_time = timer2()

print(f"Start: {time.strftime('%X', time.localtime(start_time))}")
print(f"End: {time.strftime('%X', time.localtime(end_time))}")
# We can see options in time library

print(f"Your reaction time was {end_time-start_time} seconds!")


# Represents time cpu uses to process the lines of code

input("Press enter to start")

wait_time = random.randint(1, 3)
time.sleep(wait_time)
start_time = timer3()
input("Press enter to stop")

end_time = timer3()

print(f"Start: {time.strftime('%X', time.localtime(start_time))}")
print(f"End: {time.strftime('%X', time.localtime(end_time))}")
# We can see options in time library

print(f"Your reaction time was {end_time-start_time} seconds!")
