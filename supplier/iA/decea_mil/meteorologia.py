import datetime
def cod_metar(metar):
	info_met=[]
	if metar.lower() == 'ss':
		print('meteorologia não informada atualize logo!')
	
	else:
		print ('Entre com informações de meteorologia')
		metar= input('Metar - Tecle => M ,TAF - Tecle => T , TEMPO CLIMA - Tecle => C ,')
		print ('Sua infomação será ?:',metar)
	
	if  metar.lower() == 'm':
		print('informe o METAR')
		valor = input('Localidade: ').upper()
		info_met.append(valor)
		valor = input('infomações foram coletadas de (https//met.decea.mil.br)?')
		
		if valor.lower() == 'y':
			info_met.append('https//met.decea.mil.br')
		else:
			print('informe o local da coleta de informações')
			valor = input('< alterção > informe?')
			info_met.append(valor+"<alterção>")
		

		info_met.append('Metar')
		data_hora_atual=datetime.datetime.now()
		info_met.append(data_hora_atual.strftime("%d%m%Y"))
		info_met.append(data_hora_atual.strftime("%H%M%S"))
		while True:
			valor = input('hora da extração Z')
			if len(valor)== 6:
				info_met.append(valor+"Z")
				break
			else:
				print('informe no formato padrao decea sem o Z')
		while True:
			valor = input('Vento de superfice? ')
			if len(valor)<=5 :
				info_met.append(valor+"KT")
				break
			else:
				print('verificar fatores de alterção decea sem o kt')

		while True:
			valor = input('Visibilidade? ')
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=5 :
					info_met.append(valor)
					break
				else:
					print('verificar fatores de alterção decea sem o Z')
			
		while True:
			valor = input('Teto -Nuvens? ').upper()
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=6 :
					info_met.append(valor)
					break
				else:
					print('verificar fatores de alterção decea sem o Z')
	
		while True:
			valor = input('Temperatura e orvalho? ')
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=4 :
					info_met.append(valor[:2]+"/"+valor[2:])
					break
				else:
					print('verificar fatores de alterção decea sem o /')


		while True:
			valor = input('QNH preção atmosferica ')
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=4 :
					info_met.append("Q"+valor)
					break
				else:
					print('verificar fatores de alterção decea sem o Q')

		return info_met

	if  metar.lower() == 't':
		print('informe a TAF')


		valor = input('Localidade: ').upper()
		info_met.append(valor)
		valor = input('infomações foram coletadas de (https//met.decea.mil.br)?')
		if valor.lower() == 'y':
			info_met.append('https//met.decea.mil.br')
		else:
			print('informe o local da coleta de informações')
			valor = input('< alterção > informe?')
			info_met.append(valor+"<alterção>")
			

		info_met.append('Taf')
		data_hora_atual=datetime.datetime.now()
		info_met.append(data_hora_atual.strftime("%d%m%Y"))
		info_met.append(data_hora_atual.strftime("%H%M%S"))
		while True:
			valor = input('Hora da extração Z')
			if len(valor)== 6:
				info_met.append(valor+"Z")
				break
			else:
				print('informe no formato padrao decea sem o Z')
		while True:

			valor = input('Validade. 1200 nacinal /24 iternacional? ')
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=8 :
					info_met.append(valor[:4]+"/"+valor[4:])
					break
				else:	
					print('verificar fatores da  alterção de extração decea sem a /')	


		while True:
			valor = input('Vento de superfice? ')
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=5 :
					info_met.append(valor+"KT")
					break
				else:	
					print('verificar fatores de alterção decea sem o kt')

		while True:
			valor = input('Visibilidade? ').upper()
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=5 :
					info_met.append(valor)
					break
				else:	
					print('verificar fatores de alterção decea sem o Z')

		while True:
			valor = input('Teto -Nuvens? ').upper()
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=6 :
					info_met.append(valor)
					break
				else:	
					print('verificar fatores de alterção decea sem o ex stc')

		while True:
			valor = input('Temperatura máxima TX? ')
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=6 :
					info_met.append("TX"+valor[:2]+"/"+valor[2:]+'Z')
					break
				else:	
					print('verificar fatores de alterção decea sem o so numeros')
	
		while True:
			valor = input('Temperatura mínima TN? ')
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=6 :
					info_met.append("TN"+valor[:2]+"/"+valor[2:]+'Z')
					break
				else:	
					print('verificar fatores de alterção decea sem o so numeros')
					break		

		while True:
			valor = input('Probabilidade % ')
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=3 :
					info_met.append("PROB"+valor)
					break
				else:
					print('verificar fatores de alterção decea sem o PROB')

		while True:
			valor = input('BECMG ? Y-N -variação gradual espera novas condições; ')
			if (valor.lower() == 'y'):
				info_met.append("FM")
				while True:
					valor = input('Validade. 1200 nacinal /24 iternacional? ')
					if len(valor)==8 :
						info_met.append(valor[:4]+"/"+valor[4:])
						while True:
							valore = input('Informe variação KT')
							if len(valore)<=5 :
								info_met.append(valore+"KT")
								break

							else:
								print('verificar fatores de alterção decea sem  a /')
						break
					else:
						print('verificar fatores de alterção decea sem  a /')
				break
			else:
				break
		while True:
			valor = input('FM ? Y-N -variação gradual espera novas condições; ')
			if (valor.lower() == 'y'):
				info_met.append("FM")
				while True:
					valor = input('Validade. 1200 nacinal /24 iternacional? ')
					if len(valor)==8 :
						info_met.append(valor[:4]+"/"+valor[4:])
						while True:
							valore = input('Informe variação KT')
							if len(valore)<=5 :
								info_met.append(valore+"KT")
								break

							else:
								print('verificar fatores de alterção decea sem  a /')
						break
					else:
						print('verificar fatores de alterção decea sem  a /')
				break
			else:
				break
		while True:
			valor = input('Temperatura e orvalho? ')
			if valor.lower() == 'n':
				break
			else:
				if len(valor)==4 :
					info_met.append(valor[:2]+"/"+valor[2:])
					break
				else:
					print('verificar fatores de alterção decea sem a /')
		
		while True:
			valor = input('QNH preção atmosferica ')
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=4 :
					info_met.append("Q"+valor)
					break
				else:
					print('verificar fatores de alterção decea sem o Q')
		while True:
			valor = input('Iformação do Previsor ').upper()
			if valor.lower() == 'n':
				break
			else:
				if len(valor)<=4 :
					info_met.append("RMK"+valor)
					break
				else:
					print('verificar fatores de alterção decea sem o RMK')




		return info_met
