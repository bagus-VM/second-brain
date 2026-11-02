import random
import time

# delta parameter of the CNV algorithm
DELTA = 50

# Clock implementation
# Clock has a name (name), a local time (ticks), and speed with potentially some error (speed, 1=correct speed),
class CNV:
	name = ""
	ticks = 0
	speed = 1

	# adjustment value, calculated in sync() and used in the next tick() to adjust local clock
	adjust = 0
	def __init__(self, name, initticks, speed):
		self.name = name
		self.ticks = initticks
		self.speed = speed

	# read the local clock value
	def read(self):
		return self.ticks

	# advance the lock clock by one tick (default 1, but speed value can be used to simulate frequency error)
	def tick(self):
		self.ticks += self.speed + self.adjust
		self.adjust = 0

	# The "CNV" algorithm -- note: this is just a partial implementation
	# (a) read all clocks of all nodes (using read())
	# (b) what we do here is
	#     - calculate the difference to the local clock
	#     - calculate the average of all differences (sum divided by len of nodelist)
	#     - set the adjust value to the average
	#     - next tick will adjust local clock by that adjust value.
	def sync(self, nodelist):
		self.adjust = 0
		for n in nodelist:
			diff = n.read() - self.ticks
			self.adjust += diff
		self.adjust = self.adjust / len(nodelist)


# This is a subclass of CNV to simulate a falseticker
# It returns the local clock modified by a random value
class EVILCNV(CNV):
	def read(self):
		return self.ticks + random.randint(-100,1000)
	def sync(self, nodelist):
		# do nothing
		pass


####
# Creating several node instances
# parameters: Name, initial tick value, tick speed (default=1)
a = CNV("A", 0, 1)
b = CNV("B", 0, 1)
# b = CNV("B", 40, 1)    ### to simulate a clock with initial error
c = CNV("C", 0, 1)
# c = CNV("C", 0, 1.05)    ### to simulate a clock that is 5% faster than the others.
d = CNV("D", 0, 1)
# d = EVILCNV("D", 0, 1)      ### to simulate a clock that is a falseticker ("evil")
nodes = (a,b,c,d)


realclock = 0
while True:
	# Let all clocks advance for 100 clock ticks
	for i in range(100):
		[n.tick() for n in nodes]

	# Use the CNV algorithm for synchronizing the locks
	[n.sync(nodes) for n in nodes]

	# Print all clock values, and maximum error of non-malicious nodes
	[ print(n.name, ": %.2f"%n.ticks) for n in nodes ]

	ticks = [ n.ticks for n in filter(lambda n: not isinstance(n,EVILCNV), nodes) ]
	print("nodes have clock values from %.2f to %.2f (max diff %.2f)\n" % 
		(min(ticks), max(ticks), max(ticks)-min(ticks)) )
	time.sleep(1)
	
