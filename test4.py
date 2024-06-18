s=input("Enter a scquence of integers scparated by whitespace:")

s1=s.split(" ")
s1=list(s1)

s1=[int(x) for x in s1]
c=[]
temp=[s1[0]]
for element in s1[1:]:
	if element>temp[-1]:
		temp.append(element)
	else:
		c=max (c,temp,key=len)
		temp=[element]
c=max(c,temp,key=len)


print("Length:",len(c))
print("LICS:",c)
