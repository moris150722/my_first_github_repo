n = (input("Input the total number of students (n > 0): "))
n1 =int(n) 
n2=n1//3
n3=n1-1
s = []

i=1

while i <= n1 - n2:
    if i % 3 != 0 and n2 == 0:
        s.append(i)
    elif i % 3 != 0 and n2 == 1:
        s.append(i)
        
    elif i % 3 != 0 and n2 == 2:
        s.append(i)
        
    i += 1


if i % 3 != 0 and n2 == 1:
	s=[n1]+s
elif i % 3 != 0 and n2 == 2:
	s=[n3, n1] + s

w = 2
while w <= len(s) - 1:
    s.remove(s[w])
    w += 3

if len(s)%3==1:
	s=s[-1]+s.pop(s)
elif len(s)%3==2:
	s=s[-2:]+s[0:-2]
elif len(s)%3==0:
	s=s



print(s)
