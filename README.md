# OceanZipSecureUploader

##Descrição

OceanZipSecureUploader é uma aplicação projetada para fazer upload seguro de arquivos ZIP para a API da OceanSec. Este script interage com a API para obter uma palavra-chave única, gera um token JWT com informações do usuário e uma chave criptografada MD5, e então faz o upload do arquivo ZIP.

##Como usar

- Clone este repositório.
- Execute pip install -r requirements.txt para instalar as dependências.
- Execute o script usando ```python OceanZipSecureUploader.py --folder [PastaParaZipar]```

Parâmetros
--folder: Pasta que você deseja zipar e fazer o upload.

##Funcionalidades

- Comunica-se com apisec.oceansec.com na porta 80.
- Gera uma chave única a partir de uma palavra-chave obtida via GET na API.
- Gera um token JWT contendo o nome do usuário, o cargo e a chave única.
- Zipa a pasta especificada.
- Faz o upload do arquivo ZIP usando o token JWT.


##Notas

Este script é para uso interno da OceanSec e para aqueles que têm permissão para interagir com a API da OceanSec.

##Dependências

- Python 3.x
- requests
- PyJWT
- hashlib

##Licença

MIT
