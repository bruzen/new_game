
import random
import numpy as np
import matplotlib.pyplot as plt

class Person:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.color = "blue"
		self.info = None
		self.val = x*y




def run(seed, *actions):
	people = []

	s = 5
	for i in range(s):
		for j in range(s):
			people.append(Person(i,j)) 
	
	data = {}
	data["avg"] = []	

	for i, action in enumerate(actions):
		people[i].val += 1
		sum = 0.0
		
		for j in range(len(people)):
			sum += people[j].val
		avg = sum/len(people) 

		data["avg"].append(avg)

	data["grid"] = []
	for p in people:
		item = dict(x = p.x, y = p.y, color = p.color, info = p.info, type = "Person")
		data["grid"].append(item)

	return data

def clear_cache():
	return

if __name__ == '__main__':	
	print run(100,1,2,3)



	