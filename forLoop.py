def loopFor(limit):
    import time
    for_time_start = time.time()
    counter = 1
    sum = 0
    for counter in range(1, limit+1):
        sum += counter
        counter += 1
    for_time_end = time.time()
    for_time_total = for_time_end - for_time_start
    print("For loop time: {0}" .format(for_time_total))
