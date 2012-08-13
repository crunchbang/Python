def gcd (a, b):
	while a > 0 and b > 0:
		if a > b:
			a = a % b
		else:
			b = b % a
	return a if a else b

class Jugs:
	def __init__ (self, cap):
		self.qty = 0
		self.cap = cap
	def fill (self):
		self.qty = self.cap
	def full (self):
		if self.qty == self.cap:
			return True
		else:
			return False
	def empty (self):
		if self.qty == 0:
			return True
		else:
			return False
	def drain (self):
		self.qty = 0
	def transfer (self, inp):
		rmn = self.cap - self.qty
		if inp > rmn:
			self.qty = self.cap
			return inp - rmn
		else:
			self.qty += inp
			return 0
		
def printJugs (jug1, jug2):
	print "(" + str(jug1.qty) + ", " + str(jug2.qty) + ")"

def checkfillJugs (jug1, jug2):
	jug1.qty = jug2.transfer(jug1.qty)
	if jug2.full():
		jug2.drain()
	return jug1, jug2
	
if __name__ == "__main__":
	qty1 = input("Enter the capacity of Jug 1: ")
	qty2 = input("Enter the capacity of Jug 2: ")
	cpcty = input("Enter the capacity you wish to measure out: ")
	if cpcty > max(qty1, qty2) or cpcty % gcd(qty1, qty2) != 0:
		print "Not possible!!"
		exit(0)
	jug1 = Jugs(min(qty1, qty2))
	jug2 = Jugs(max(qty1, qty2))
	while jug2.qty != cpcty:
		if jug1.empty():
			jug1.fill()
			printJugs(jug1, jug2)
		checkfillJugs(jug1, jug2)
		printJugs(jug1, jug2)




		


