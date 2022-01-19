# Authors: Declan Holingworth & Nishant Tewari
# Student #: 190765210 & 190684430
# Date: January 10th, 2022


import time

n = 50 
n2 = 100 
n3 = 150


# Segment 1
start = time.time()

sum = 0
for i in range(n):
    sum += 1

end = time.time()
totalRunTime = end - start

print(totalRunTime)


# Segment 2

start = time.time()

sum = 0
for i in range(n):
    for j in range(n):
        sum += 1

end = time.time()
totalRunTime = end - start

print(totalRunTime)



# Segment 3

start = time.time()
sum = 0
for i in range(n):
    for j in range(n*n):
        sum += 1

end = time.time()
totalRunTime = end - start

print(totalRunTime) 

# Segment 4
start = time.time()

sum = 0
for i in range(n): #O(n)
    for j in range(i): #(n^2)
        sum += 1

end = time.time()
totalRunTime = end - start

print(totalRunTime) 



# Segment 5

start = time.time()

sum = 0
for i in range(n): # O(n)
    for j in range(i*i): #o(n^2)
        for k in range(j): 
            sum += 1

end = time.time()
totalRunTime = end - start

print(totalRunTime) 


# Segment 6

start = time.time()

sum = 0
for i in range(n): #O(n)
    for j in range(i*i): #o(n^2)
        if (j%i == 0):
            for k in range(j):
                sum += 1

end = time.time()
totalRunTime = end - start

print(totalRunTime) 
