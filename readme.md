# Simulador IoT para Monitoramento de Pacientes

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9.7-blue?logo=python&logoColor=white" alt="Python 3.9.7">
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen" alt="Status: Concluído">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License: MIT">
</p>

---

## Sumário

- [📖Sobre o Projeto](#-sobre-o-projeto)
- [🎯Objetivos](#-objetivos)
- [💻Tecnologias](#-tecnologias)
- [🏛️Arquitetura e Design](#-arquitetura-e-design)
- [🏗️Funcionalidades Principais](#-funcionalidades-principais)
- [🔗Integração com o Sistema InfraMed](#-integração-com-o-sistema-inframed)
- [📊Diferenciais Técnicos](#-diferenciais-técnicos)
- [🗂️Estrutura do Projeto](#-estrutura-do-projeto)
- [🔍Pré-requisitos e Instalação](#-Pré-requisitos-e-instalação)
- [🚀Como Executar](#-como-executar)
- [⚙️Configuração](#-configuração)
- [💡Contexto do Projeto](#-contexto-do-projeto)
- [✍️Autor](#️-autor)

---

## 📖 Sobre o Projeto

O **Simulador IoT para Monitoramento de Pacientes** é um componente essencial do ecossistema InfraMed, desenvolvido para emular o comportamento de dispositivos IoT em ambientes hospitalares. Este simulador facilita a validação e o teste da comunicação entre sensores conectados e o backend da aplicação, assegurando a robustez do sistema de monitoramento contínuo de sinais vitais. Ao gerar e enviar dados simulados de forma automatizada, o projeto permite a avaliação de cenários reais sem a necessidade de hardware físico, contribuindo para uma implementação mais segura e eficiente da saúde digital.

---

## 🎯 Objetivos

- **Teste de Integração:** Validar a comunicação HTTP entre dispositivos IoT e a API REST do backend.
- **Simulação Realista:** Reproduzir leituras de sinais vitais dentro de parâmetros médicos aceitáveis.
- **Suporte ao Desenvolvimento:** Auxiliar na depuração e otimização do sistema de notificações e armazenamento de dados.
- **Demonstração de Conceito:** Ilustrar a viabilidade da IoT em contextos de saúde, preparando para integrações com ESP32 e outros microcontroladores.

---

## 💻 Tecnologias

- **Python 3.9+:** Linguagem de programação principal, escolhida por sua simplicidade e ecossistema robusto para scripts e automação.
- **Requests:** Biblioteca padrão de mercado para realizar requisições HTTP de forma simples e eficiente.
- **JSON:** Módulo nativo para manipulação de dados no formato JSON, essencial para a comunicação com a API.
- **Time & Random:** Módulos nativos para controle de tempo e geração de dados aleatórios, simulando variações naturais nos sinais vitais.

---

## 🏛️ Arquitetura e Design

O simulador segue uma arquitetura procedural e modular, otimizada para execução contínua e baixa complexidade. Os componentes principais incluem:

- **Módulo de Geração de Dados:** Algoritmo que produz leituras aleatórias baseadas em faixas fisiológicas, assegurando realismo médico.
- **Módulo de Comunicação:** Interface HTTP que envia dados para o endpoint designado, simulando o protocolo de dispositivos IoT.
- **Loop de Execução:** Estrutura de repetição infinita com pausa configurável, permitindo testes prolongados e monitoramento em tempo real.

Essa abordagem garante escalabilidade e facilidade de manutenção, alinhando-se aos princípios de Clean Code e modularidade.

---

## 🏗️ Funcionalidades Principais

- **Simulação de Sinais Vitais:** Suporte a três tipos de dados: temperatura corporal, frequência cardíaca e pressão arterial.
- **Envio Automatizado:** Transmissão periódica de leituras via método POST, com intervalo padrão de 5 segundos.
- **Simulação de Faixas:** Valores gerados respeitam limites médicos (ex.: temperatura entre 30.0°C e 42.0°C para testes abrangentes).
- **Logging em Tempo Real:** Exibição detalhada no console dos dados enviados e respostas da API, incluindo JSON de retorno.
- **Tratamento de Erros:** Gestão de falhas de conexão e códigos de resposta HTTP inadequados.
- **Simulador de Erros:** Versão adicional (SimuladorIOT_Error.py) para testar cenários de erro, com IDs de atendimento aleatórios e valores inválidos/extremos.

---

## 🔗 Integração com o Sistema InfraMed

O simulador interage diretamente com o backend InfraMed através do endpoint `/api/leituras/atendimento/{atendimentoId}`, enviando payloads JSON estruturados conforme o contrato da API.

Exemplo de payload:

```json
{
  "valor": 36.5,
  "tipoDado": "TEMPERATURA",
  "unidadeMedida": "GRAUS_CELSIUS"
}
```

Essa integração possibilita:

- **Teste de Persistência:** Verificação do armazenamento correto no banco de dados MySQL.
- **Validação de Regras de Negócio:** Avaliação da geração de notificações para valores fora do padrão.
- **Monitoramento Contínuo:** Simulação de cenários de internação, com dados associados a pacientes e atendimentos específicos.

---

## 📊 Diferenciais Técnicos

- **Precisão Médica:** Algoritmos baseados em parâmetros fisiológicos, assegurando testes fiéis à realidade clínica.
- **Baixo Acoplamento:** Dependências mínimas, facilitando execução em diversos ambientes.
- **Conformidade com Padrões:** Adesão a protocolos HTTP REST, compatível com APIs modernas.
- **Extensibilidade:** Estrutura preparada para inclusão de novos tipos de sensores e métricas.

---

## 🗂️ Estrutura do Projeto

```
SimuladorIoTMonitoramentoPacientes/
├── SimuladorIOT.py          # Simulador do IoT (Caminho Feliz)
├── SimuladorIOT_Error.py    # Simulador do IoT (Tratamento de Erros)
└──readme.md                 # Documentação do projeto
```

---

## 🔍 Pré-requisitos e Instalação

### Pré-requisitos

- **Python 3.7.9** ou versão superior instalada no sistema.
- **Biblioteca requests:** Instalar via `pip install requests`.
- **Backend InfraMed:** Sistema rodando e acessível via HTTP (padrão: `http://localhost:8080`).
- **Atendimento Configurado:** Garantir que o ID de atendimento especificado exista no banco de dados.

### Instalação

1. **Clonagem do Repositório:**

   ```bash
   git clone https://github.com/matheus05dev/SimuladorIoTMonitoramentoPacientes.git
   cd SimuladorIoTMonitoramentoPacientes
   ```

2. **Instalação de Dependências:**
   ```bash
   pip install requests
   ```

## 🚀 Como Executar

1. **Preparação do Ambiente:**

   - Inicie o backend InfraMed na porta 8080.
   - Verifique a conectividade com o endpoint de leituras.

2. **Execução do Simulador (Caminho Feliz):**

   ```bash
   python SimuladorIOT.py
   ```

3. **Execução do Simulador (Tratamento de Erros):**

   ```bash
   python SimuladorIOT_Error.py
   ```

4. **Monitoramento:**

   - Observe os logs no console para confirmar o envio de dados.
   - Utilize ferramentas como Postman ou o Swagger do backend para validar o recebimento.

5. **Interrupção:**
   - Pressione `Ctrl + C` para encerrar a execução.

---

## ⚙️ Configuração

O arquivo `SimuladorIOT.py` permite customizações diretas:

- **ATENDIMENTO_ID:** Altere para o ID desejado (ex.: `ATENDIMENTO_ID = 2`).
- **API_BASE_URL:** Modifique para apontar para outro host ou porta.
- **Intervalo de Envio:** Ajuste o `time.sleep(5)` para alterar a frequência (em segundos).
- **Tipos de Dados:** Expanda a lista `TIPOS_DADO` para incluir novos sinais vitais.

Para cenários avançados, considere a criação de subclasses ou módulos adicionais para simular múltiplos dispositivos simultaneamente.

---

## 💡 Contexto do Projeto

Este projeto constitui uma parcela significativa do Trabalho de Conclusão de Curso (TCC) do curso Técnico de Desenvolvimento de Sistemas, ministrado pela Escola SENAI 403 "Antônio Ermírio de Moraes" em Alumínio-SP. Desenvolvido para fins de uso sem o equipamento físico, o Simulador IoT exemplifica a aplicação prática de conceitos de Internet das Coisas (IoT) no setor da saúde, promovendo a inovação e a eficiência em ambientes hospitalares. Além de seu valor acadêmico, o projeto serve como referência para profissionais em desenvolvimento de software, destacando a importância da integração entre hardware e software na saúde conectada.

---

## ✍️ Autor

**Matheus Nunes da Silva**

- **GitHub:** [https://github.com/matheus05dev](https://github.com/matheus05dev)

---
