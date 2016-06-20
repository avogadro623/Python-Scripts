#! python
import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))
#print(input('What is your name?'))
#x=input('What is your name?')
#print ('Your name is ' + x)
y = 0
s=0
while y < 5:
    y += 1
    z = (int(input("Enter a number: ")))
    s = s +z
print(s)
m_array = list()
num = input("Enter how many elements you want:")
#print ('Enter numbers in array:')
for i in range(int(num)):
    n = input("num :")
    m_array.append(int(n)*int(n))
print ('ARRAY: ',m_array)
print (' SORTED ARRAY: ', sorted(m_array))
