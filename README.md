# Médico Digital

Este projeto é um sistema de diagnóstico médico digital que coleta informações do usuário sobre sintomas e retorna possíveis diagnósticos com base em um sistema especialista. O frontend é construído com React, enquanto o backend é construído com Flask.

## Estrutura do Projeto

- **Frontend**: React
- **Backend**: Flask

## Como Funciona

1. O usuário é recebido por uma tela de boas-vindas e é solicitado a inserir seu nome.
2. O usuário responde a um questionário sobre seus sintomas.
3. Os dados do questionário são enviados para o backend.
4. O backend processa os dados e retorna um possível diagnóstico.
5. O diagnóstico é exibido na tela de resultados.

## Configuração e Execução

### Backend

1. **Clone o repositório:**

    ```bash
    git clone <URL-do-repositório>
    cd <diretório-do-repositório>
    ```

2. **Navegue até o diretório do backend:**

    ```bash
    cd medico-digital-backend
    ```

3. **Crie e ative um ambiente virtual (venv):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # Esse é o comando para mac, no Windows use `venv\Scripts\activate`
    ```

4. **Instale as dependências:**

    ```bash
    pip3 install Fask
    pip3 install flask_cors
    ```

5. **Execute o servidor Flask:**

    ```bash
    python main.py
    ```

    O servidor backend estará rodando em `http://localhost:5000`.

### Frontend

1. **Navegue até o diretório do frontend:**

    ```bash
    cd medico-digital-frontend
    ```

2. **Instale as dependências:**

    ```bash
    npm install
    ```

3. **Inicie o servidor de desenvolvimento do React:**

    ```bash
    npm start
    ```

    O servidor frontend estará rodando em `http://localhost:3000`.

## Estrutura dos Arquivos

### Backend (`main.py`)

- **`ExpertSystem`**: Classe que contém a lógica do sistema especialista para calcular a pontuação de correspondência de sintomas e determinar possíveis diagnósticos.
- **`calculate_match_score`**: Método que calcula a pontuação de correspondência entre os dados do usuário e uma doença.
- **`diagnose`**: Método que determina o diagnóstico com base na pontuação de correspondência mais alta.
- **API `/diagnose`**: Rota POST que recebe os dados do usuário, processa-os e retorna o diagnóstico.

### Frontend

- **`App.js`**: Componente principal que gerencia o fluxo de etapas (boas-vindas, questionário, resultados).
- **`Welcome.js`**: Componente de boas-vindas onde o usuário insere seu nome.
- **`Questionnare.js`**: Componente de questionário onde o usuário responde às perguntas sobre seus sintomas.
- **`Results.js`**: Componente de resultados onde o diagnóstico é exibido.

### Estilização

As cores e o layout foram escolhidos para refletir uma interface amigável para a área da saúde, utilizando tons de creme, verde e azul.

- **`App.css`**: Arquivo CSS que contém as regras de estilo para todos os componentes.

## Exemplos de Uso

### Dados do Usuário

Caso queira testar, o endpoint via Postman ou Insomnia basta bater na rota *http://localhost:5000/diagnose* , segue exemplo de dados do usuário enviados para o backend:

```json
{
    "fever": "Yes",
    "cough": "Yes",
    "fatigue": "Yes",
    "difficultyBreathing": "Yes",
    "age": 35,
    "gender": "Female",
    "bloodPressure": "Normal",
    "cholesterolLevel": "Normal"
}
