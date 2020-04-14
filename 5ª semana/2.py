def éPrimo(k):
	i=k
	cont=0
	while(i>0):
		if(k%i==0):
			cont+=1
		i-=1
	if(cont==2):
		return 1
	else:
		return 0

def maior_primo(n):
	i=maior=2
	while(i<=n):
		if(éPrimo(i)==1):
			maior=i
		i+=1
	return maior