larg=int(input("digite a largura: "))
alt=int(input("digite a altura: "))
i=0
while i<alt:
	j=0
	while j<larg:
		if i==0 or i==(alt-1) or j==0 or j==(larg-1):
			print("#",end='')
		else:
			print(" ",end='')
		j+=1
	i+=1
	print(end='\n')
