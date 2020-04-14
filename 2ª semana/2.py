x = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dia = x//60//60//24

hora=(x//60//60)%24

minuto= (x//60)%60

segundo=x%60

print(dia," dias ",hora," horas ",minuto," minutos",segundo," segundos.")