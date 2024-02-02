
def bin_to_hex(binary):
	decimal= int(binary, 2)
	hex_value=hex(decimal)[2:] #remover o prefixo 0x
	return hex_value

def hex_to_bin(hex_value):
	decimal=int(hex_value, 16)
	binary=bin(decimal)[2:] #remove o prefixo '0b'
	return binary

def main(binary): 
	binary_numbers=[]
	binary_input=(binary)
	binary_numbers.append(binary_input)
	hex_numbers=bin_to_hex(binary_input)
	print('Lendo aqui!->',str(hex_numbers))

def hexa_main(hexadecimal): 
	hex_numbers=[]
	hex_input=(hexadecimal)
	hex_numbers.append(hex_input)
	binario_numbers=hex_to_bin(hex_input)
	print('Lendo aqui binário!->',str(binario_numbers))
	with open('hex_numbers.pyc',w) as file:
		for hex_num in hex_numbers:
 			file.write(hex_num +'\n')
