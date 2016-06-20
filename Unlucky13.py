#! python
import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))
#print(input('What is your name?'))
#x=input('What is your name?')
#print ('Your name is ' + x)
h1 = 0
h2 = 0
m1 = 0
m2 = 0
z = 0
count = 0
count1 = 0
z_max=0
if h1 == 0:
	for h2 in range (1,10):
		for m1 in range (0,6):
			for m2 in range(0,10):
   				count=count+1
   				z=h1+h2+m1+m2
   				if (z>z_max):
   					z_max=z
   					h1max=h1
   					h2max=h2
   					m1max=m1
   					m2max=m2
   				if z==13:
   					#print(z)
   					#print (h1,h2,m1,m2)
   					count1=count1+1
h1=h1+1
for h2 in range (0,2):
	for m1 in range (0,6):
		for m2 in range(0,10):
			count=count+1
			z=h1+h2+m1+m2
			if z==13:
				#print (h1,h2,m1,m2)
				count1=count1+1   					
print(round(count1/count*100,2),"%")
print(h1max,h2max,":",m1max,m2max)