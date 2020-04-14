n = input("Digite o valor de n: ")
num=int(n)
tam=len(n)
cont=0
soma=0
while cont<tam:
	soma+=num%10
	num=num//10
	cont+=1
print(soma)