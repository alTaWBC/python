import time

clocks = {"perf_counter", "monotonic", "process_time", "time"}

for clock in sorted(clocks):
    print("Info in", clock)
    print(time.get_clock_info(clock))
    print()
