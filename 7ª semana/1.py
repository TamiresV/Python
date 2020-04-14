larg=int(input("digite a largura: "))
alt=int(input("digite a altura: "))
i=0
while i<alt:
	j=0
	while j<larg:
		print("#",end='')
		j+=1
	i+=1
	print(end="\n")