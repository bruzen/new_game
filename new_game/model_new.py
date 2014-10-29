
import random
import numpy as np
import matplotlib.pyplot as plt

class Person:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.val = x*y

people = []

s = 5
for i in range(s):
	for j in range(s):
		people.append(Person(i,j))
		
for k in range(len(people)):
	print people[k].val

#print people
	