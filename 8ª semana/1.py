def remove_repetidos(lista):
	lista.sort()
	nova=[]
	nova.append(lista[0])
	for i in lista:
		rep=True
		for j in nova:
			if j==i:
				rep=False
		if rep==True:
			nova.append(i)
	return nova