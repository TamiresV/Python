def computador_escolhe_jogada(n,m):
	i=m
	if n<m:
		pecas=n
	else:
		pecas=m
	while i>0:
		if (n-i)%(m+1)==0:
			pecas=i
			break
		i-=1
	return pecas

def usuario_escolhe_jogada(n,m):
	pecas=0
	while pecas<=0 or (pecas>n and pecas>m):
		pecas=int(input("\nQuantas peças você vai tirar? "))
		if pecas<=0 or (pecas>n and pecas>m):
			print("\nOops! Jogada inválida! Tente de novo.")	
	return pecas

def campeonato():
	usuario=0
	computador=0
	rod=1
	while rod<4:
		print("\n**** Rodada ", rod," ****")
		ganhou=partida()
		rod+=1
		imprime_ganhador(ganhou)
		if ganhou==1:
			usuario+=1
		elif ganhou==2:
			computador+=1

	print("\n**** Final do campeonato! ****")
	print("\nPlacar: Você ", usuario, " X ",computador," Computador")


def partida():
	n=int(input("\nQuantas peças? "))
	m=int(input("Limite de peças por jogada? "))
	tirou=0
	#usuario=1 computad=2
	if n% (m+1) == 0:
		print("\nVocê começa!")
		tirou=usuario_escolhe_jogada(n,m)
		jogou=1
		print("\nVocê tirou ", tirou, " peça(s).")
	else:
		print("\nComputador começa!")
		tirou=computador_escolhe_jogada(n,m)
		jogou=2
		print("\nO computador tirou", tirou, " peça(s).")
	n=n-tirou

	while n>0:
		print("Agora resta(m) ", n," peça(s) no tabuleiro.")
		if jogou==1:
			tirou=computador_escolhe_jogada(n,m)
			jogou=2
			print("\nO computador tirou", tirou, " peça(s).")
		elif jogou==2:
			tirou=usuario_escolhe_jogada(n,m)
			jogou=1
			print("\nVocê tirou ", tirou, " peça(s).")
		n=n-tirou
	return jogou


def imprime_ganhador(ganhou):
	if ganhou==1:
		print("Fim do jogo! Você ganhou!")
	elif ganhou==2:
		print("Fim do jogo! O computador ganhou!")

def main():
	op = 0
	print("Bem-vindo ao jogo do NIM! Escolha:")
	while op!=1 and op!=2:
		op=int(input("\n1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
	if op==1:
		print("\nVocê escolheu uma partida isolada")
		ganhou=partida()
		imprime_ganhador(ganhou)
	elif op==2:
		print("\nVocê escolheu um campeonato")
		campeonato()

main()