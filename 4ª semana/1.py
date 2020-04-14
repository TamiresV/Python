n = int(input("Digite o valor de n: "))
aux=n
if n==0:
	res=1
else:
	while n>1:
		aux=aux*(n-1)
		n=n-1
	res=aux
print(res)
