import time

inital = time.time()
print("hello subhash")
print( "while loop ran in  ", time.time()- inital, "seconds")

time.sleep(2)
# get 2 second sleep

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

