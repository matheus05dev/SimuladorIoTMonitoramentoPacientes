import requests
import json
import time
import random

# ID do atendimento que você quer simular (aleatório de 1 a 99 para testar diferentes IDs)
ATENDIMENTO_ID = random.randint(1, 99)

# A URL da API base, com a variável de caminho
API_BASE_URL = f"http://localhost:8080/api/leituras/atendimento/{ATENDIMENTO_ID}"

# Lista de tipos de dados para simular o enum
TIPOS_DADO = ["TEMPERATURA", "FREQUENCIA_CARDIACA", "PRESSAO_ARTERIAL"]


def gerar_dados_aleatorios_com_erros():
    """Gera um JSON de leitura com tipo de dado, valor e unidade aleatórios, incluindo casos de erro."""

    tipo_dado = random.choice(TIPOS_DADO)
    valor = 0
    unidade = "string"

    # Introduzir erros aleatoriamente
    if random.random() < 0.3:  # 30% chance de erro
        # Erro: valor negativo ou extremo para testar validações
        if tipo_dado == "TEMPERATURA":
            valor = round(random.uniform(-10.0, 50.0), 2)  # Valores extremos
            unidade = "CELSIUS"
        elif tipo_dado == "FREQUENCIA_CARDIACA":
            valor = random.randint(-50, 200)  # Valores negativos ou altos
            unidade = "BPM"
        elif tipo_dado == "PRESSAO_ARTERIAL":
            valor = random.randint(-100, 300)  # Valores inválidos
            unidade = "MMHG"
    else:
        # Valores normais
        if tipo_dado == "TEMPERATURA":
            valor = round(random.uniform(30.0, 42.0), 2)
            unidade = "CELSIUS"
        elif tipo_dado == "FREQUENCIA_CARDIACA":
            valor = random.randint(40, 150)
            unidade = "BPM"
        elif tipo_dado == "PRESSAO_ARTERIAL":
            valor = random.randint(70, 200)
            unidade = "MMHG"

    return {"valor": valor, "tipoDado": tipo_dado, "unidadeMedida": unidade}


while True:
    dados_json = gerar_dados_aleatorios_com_erros()
    print(f"Enviando dados para o atendimento {ATENDIMENTO_ID}: {dados_json}")

    try:
        # Envia os dados para a API usando o método POST
        response = requests.post(API_BASE_URL, json=dados_json)

        # Verifica se a requisição foi bem-sucedida (status 200 ou 201)
        if response.status_code in [200, 201]:
            print("Dados enviados com sucesso!")
            print("Resposta da API:", response.json())
        else:
            print(f"Erro ao enviar dados: {response.status_code}")
            print("Resposta de erro:", response.text)

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")

    # Espera um tempo antes de enviar a próxima requisição
    time.sleep(5)  # Envia uma nova medição a cada 5 segundos
