import math,random,json,os

def bin_to_hex(binary):
	decimal= int(binary, 2)
	hex_value=hex(decimal)[2:] #remover o prefixo 0x
	return hex_value

def hex_to_bin(hex_value):
	decimal=int(hex_value, 16)
	binary=bin(decimal)[2:] #remove o prefixo '0b'
	return binary

def main(binary):
	f_save=input 

	binary_numbers=[]
	binary_input=(binary)
	binary_numbers.append(binary_input)
	hex_numbers=bin_to_hex(binary_input)
	print('Lendo aqui send hexa!->',str(hex_numbers))
	#dados=str(hex_numbers)

	dados={
		"registro esperado":binary_numbers,
		"titulo":"api_qualific Peson",
		'lesson':"criate aprendizado",
		"interactions":"user admin",
		"hex":hex_numbers,
		"data":"data_atual"
		}

	def save(dados):
		json_path='api_hexa_path.json'
		with open(json_path,"w") as arquivo:
			json.dump(dados,arquivo)

	f_save=input('Salvar? [ sim ]= y  -  [ nao ]= n :?')
	if f_save=='y':
		save(dados)
		print("Ariquivo salvo!")

def hexa_main(hexadecimal): 
	hex_numbers=[]
	hex_input=(hexadecimal)
	hex_numbers.append(hex_input)
	binario_numbers=hex_to_bin(hex_input)
	print('Lendo aqui send binário!->',str(binario_numbers))



'''
	hexa_api_path='api_hex_path.txt'

	with open(hexa_api_path,w) as file:
		for hex_num in hex_numbers:
 			file.write(hex_num +'\n')


    json_path='arquivo_Artificial1.json'
    
    with open(json_path,'r') as json_file:
        dados=json.load(json_file)
   
    return JsonResponse({'dados': dados})
 '''
