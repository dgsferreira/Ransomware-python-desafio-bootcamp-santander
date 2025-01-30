# Ransomware-python-desafio-bootcamp-santander

import os
from pathlib import Path
import pyaes

# Caminho do arquivo criptografado
encrypted_file_path = Path("teste.txt.ransomwaretroll")

# Verifica se o arquivo existe
if not encrypted_file_path.exists():
    raise FileNotFoundError(f"O arquivo {encrypted_file_path} não foi encontrado.")

# Abre o arquivo criptografado e lê os dados
with open(encrypted_file_path, "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# Chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografa os dados
try:
    decrypted_data = aes.decrypt(encrypted_data)
except Exception as e:
    raise RuntimeError("Erro ao descriptografar o arquivo.") from e

# Remove o arquivo criptografado
try:
    os.remove(encrypted_file_path)
except Exception as e:
    raise RuntimeError(f"Erro ao remover o arquivo criptografado: {e}")

# Cria o arquivo descriptografado
decrypted_file_path = Path("teste.txt")
with open(decrypted_file_path, "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

print(f"Arquivo descriptografado com sucesso: {decrypted_file_path}")
