def loopWhile(limit):
    import time
    while_time_start = time.time()
    counter = 1
    sum = 0
    while counter != (limit+1):
        sum += counter
        counter += 1
    while_time_end = time.time()
    while_time_total = while_time_end - while_time_start
    print("While loop time: {0}" .format(while_time_total))
