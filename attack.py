import time
from pwn import *

# replace this with your own function
def compare(PIN):
	for i in range(100):
		password = '12345678'
	
		if len(PIN) != len(password):
			continue
	
		for i in range(len(PIN)):
			if PIN[i] != password[i]:
				continue
			time.sleep(0.001)
	
		continue

def calc(param, func):
	start = time.time()
	func(param)
	end = time.time()
	return end - start

def solve():
	size = 8
	PIN = ['0' for i in range(size)]
	for i in range(size):
		res = []
		for val in range(10):
			PIN[i] = str(val)
			process_time = calc(''.join(PIN), compare)
			res.append(process_time)

		minVal = 0
		minIdx = 0
		for j in range(10):
			if res[j] > minVal:
				minVal = res[j]
				minIdx = j
		PIN[i] = str(minIdx)
		
	return ''.join(PIN)

sol = solve()
print(sol)
