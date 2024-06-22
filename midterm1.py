i,j=9,9
while 3<=j<=9 :
	while   1<=i<=9:
		print(i,"x",j,"=",i*j,end="\t")
		print(i,"x",(j-1),"=",i*(j-1),end="\t")
		print(i,"x",j-2,"=",i*(j-2),end="\n")
		i=i-1
	print()
	i=9
	j=j-3
