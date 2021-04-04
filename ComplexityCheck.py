import time
start_time = time.time()
for i in range(0,200):
    print(i)
    time.sleep(0.1)
    # count = 0
    # for j in range(0, 500):
    #     print(j)
    #     count = count + j
    #     print(count)
count = 0
for j in range(0,100000):
    print(j)
    count = count + j
    print(count)

print("--- %s seconds ---" % (time.time() - start_time))
#--- 0.6874969005584717 seconds ---
