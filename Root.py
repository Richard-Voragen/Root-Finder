import itertools
import time

#Desktop/Stuff/Python
i = 0
amt = 0
final = []
collection = []

def help():
	print ""
	print "Please select manual by typing Root.manual or input the numbers into Root.collection by typing none and type Root.solve()."
	print "To multiply set Root.num1 and Root.num2 to the desired polynomials and type Root.multiply()."
	print "Feel free to type Root.help to repeat this message."
	print ""

def manual():
	model = input("The numbers are: ")
	collection = [model]
	while model != "done":
		model = input("The numbers are: ")
		if model == 000:
			solve()
			break
		else:
			collection.append(model)
			print collection

def solve(collection):
	t0 = time.time()
	i = 0
	amt = 0
	final = []
	while len(collection) > 3:

		print (collection[len(collection) - 1])
		n = collection[len(collection) - 1]
		if n < 0:
			n *= -1
			amt += 1

		factors = [5]
		factors[:] = []

		flatten_iter = itertools.chain.from_iterable
		factor = set(flatten_iter((i, n//i)
		            for i in range(1, int(n**0.5)+1) if n % i == 0))
		for x in factor:
			pos = x * 1.0
			factors.append(pos / collection[0])
			neg = x * -1.0
			factors.append(neg / collection[0])
			amt += 6
		#print factors

		rem = 5
		eqn = [5]
		eqn[:] = []
		eqn = [collection[0]]

		for x in factors:
			a = 0
			rem = int(collection[a])
			while a < len(collection) - 1:
		  	    rem = x * rem + int(collection[a + 1])
		  	    amt += 1
		  	    eqn.append(rem)
		  	    a += 1

		  	if rem == 0:
		    		#print "Finished"
		    		final.append(int(x))
		    		del eqn[len(eqn) - 1]
		    		break
		    	else:
		    		#print "Failed"
		    		eqn[:] = []
		    		eqn = [collection[0]]

		collection[:] = []
		for x in eqn:
			collection.append(x)

	final.append(collection)
	t1 = time.time()
	print "|"
	print "|"
	print "|"
	tme = t1 - t0
	print "Complete!"
	print "It took me " + str(tme) + " seconds to solve " + str(amt) + " equations!"
	print final
	print "|"
	print "|"
	print "|"


def multiply(num1, num2):
	res = [ sum( row[i] 
             for row
             in [ [0]*o2
                   +[i1*i2 for i1 in num1]
                   +[0]*(len(num1)-o2)
                  for o2,i2
                  in enumerate(num2)
                ]
             )
        for i
        in range( len(num1)+len(num2)-1 )
      ]
	print res

help()