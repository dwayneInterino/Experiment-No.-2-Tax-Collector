from forLoop import loopFor
from whileLoop import loopWhile
import time
input = int(input("Input a number: "))

time_start = time.time()
loopWhile(input)
time_end = time.time()
time_total = time_end - time_start
print("While loop time: {0}" .format(time_total))

time_start = time.time()
loopFor(input)
time_end = time.time()
time_total = time_end - time_start
print("For loop time: {0}" .format(time_total))
