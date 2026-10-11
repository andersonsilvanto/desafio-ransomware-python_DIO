import os
import pyaes

## nome do arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave de criptografia (deve ser exatamente a mesma)
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## descriptografar o arquivo
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo original recuperado
new_file = "teste.txt"
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
