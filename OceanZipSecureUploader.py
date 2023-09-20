import requests
import jwt
import hashlib
import zipfile
import os

# Função para gerar o JWT
def generate_jwt(secret, keyj_word):
    payload = {
        'Nome': 'Lucas Silva',
        'Cargo': 'Developer',
        'keyj': hashlib.md5(keyj_word.encode()).hexdigest()
    }
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token

# Função para zipar a pasta
def zip_folder(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))

# Ponto de entrada principal
if __name__ == "__main__":
    # Realizar GET na API para obter a palavra chave
    response = requests.get("http://apisecx.oceansec.com:80/get-keyj")
    if response.status_code != 200:
        print("Falha ao se comunicar com a API.")
        exit(1)

    keyj_word = response.text
    
    # Gerar JWT
    secret = 'OceanSecKEYJWt'
    token = generate_jwt(secret, keyj_word)

    # Zipar pasta passada como argumento
    folder_path = input("Digite o caminho da pasta para zipar: ")
    zip_name = "archive.zip"
    zip_folder(folder_path, zip_name)

    # Realizar upload do arquivo ZIP
    with open(zip_name, 'rb') as f:
        files = {'file': f}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post("http://apisecx.oceansec.com:80/uploadjwt", files=files, headers=headers)
        
        if response.status_code == 200:
            print("Arquivo enviado com sucesso!")
        else:
            print(f"Falha ao enviar o arquivo: {response.text}")
