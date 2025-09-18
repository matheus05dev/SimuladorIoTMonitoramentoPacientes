import requests
import json
import time
import random

# ID do atendimento que você quer simular
ATENDIMENTO_ID = 1

# A URL da API base, com a variável de caminho
API_BASE_URL = f"http://localhost:8080/api/atendimento/{ATENDIMENTO_ID}/leituras"

# Lista de tipos de dados para simular o enum
TIPOS_DADO = ["TEMPERATURA", "FREQUENCIA_CARDIACA", "PRESSAO_ARTERIAL"]


def gerar_dados_aleatorios():
    """Gera um JSON de leitura com tipo de dado, valor e unidade aleatórios."""

    tipo_dado = random.choice(TIPOS_DADO)
    valor = 0
    unidade = "string"

    if tipo_dado == "TEMPERATURA":
        valor = round(random.uniform(36.0, 40.0), 2)
        unidade = "CELSIUS"
    elif tipo_dado == "FREQUENCIA_CARDIACA":
        valor = random.randint(60, 120)
        unidade = "BPM"
    elif tipo_dado == "PRESSAO_ARTERIAL":
        # Um valor genérico para simplificar. O ideal seria ter dois valores (sistólica/diastólica)
        valor = random.randint(90, 140)
        unidade = "MMHG"

    return {"valor": valor, "tipoDado": tipo_dado, "unidadeMedida": unidade}


while True:
    dados_json = gerar_dados_aleatorios()
    print(f"Enviando dados para o atendimento {ATENDIMENTO_ID}: {dados_json}")

    try:
        # Envia os dados para a API usando o método POST
        response = requests.post(API_BASE_URL, json=dados_json)

        # Verifica se a requisição foi bem-sucedida (status 200 ou 201)
        if response.status_code in [200, 201]:
            print("Dados enviados com sucesso!")
        else:
            print(f"Erro ao enviar dados: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")

    # Espera um tempo antes de enviar a próxima requisição
    time.sleep(5)  # Envia uma nova medição a cada 5 segundos
