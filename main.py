from forLoop import loopFor
from whileLoop import loopWhile
import time
input = int(input("Input a number: "))

while_time_start = time.time()
loopWhile(input)
while_time_end = time.time()
while_time_total = while_time_end - while_time_start
print("While loop time: {0}" .format(while_time_total))

for_time_start = time.time()
loopFor(input)
for_time_end = time.time()
for_time_total = for_time_end - for_time_start
print("For loop time: {0}" .format(for_time_total))
