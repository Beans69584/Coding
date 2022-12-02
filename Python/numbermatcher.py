import random
import time
# time code execution
start_time = time.time()
tries = 1
count = 1
number = int(input("Enter the number between 1 and 1000000 "))
while count > 0:
    guess = random.randint(1,1000000)
    if guess == number:
        print("Got it in",str(tries) + " tries")
        count = count - 1
    else:
        tries = tries + 1
print("Time taken to execute the code is %s seconds" % (time.time() - start_time))