# With the concept of default parameters in mind, the goal of this assignment is to write a single function, randInt() that takes up to 2 arguments.
import random

def randInt(min = 0, max = 100):
    if min > max or max < min:
        return False
    num = random.randint(min, max)
    return num

print(randInt())
print(randInt(max=50)) 	   
print(randInt(min=50)) 	    
print(randInt(min=50, max=500)) 
print(randInt(min=150))

print(randInt(min=1000, max=10000))
print(randInt(20, 2000))