# Professor Virtual

Esta é uma aplicação web simples utilizando Flask e a API do OpenAI. A aplicação permite que os usuários façam perguntas e recebam respostas de um "professor virtual".

## Funcionalidades

- Enviar perguntas ao modelo de IA usando a API do OpenAI.
- Receber respostas detalhadas simulando um professor experiente.
- Interface web estilizada com Tailwind CSS.
- Indicador de loading e gerenciamento de estado de envio.

## Requisitos

- Python 3.7 ou superior
- Conta na OpenAI com uma chave de API válida

## Instalação

Siga os passos abaixo para configurar e rodar a aplicação localmente.

### 1. Clone o repositório

```bash
git clone https://github.com/seu_usuario/nome_do_repositorio.git
cd nome_do_repositorio
```

### 2. Crie e ative um ambiente virtual (recomendado)
No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Crie um arquivo .env
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

``` API_KEY=your_openai_api_key_here ``` 

Substitua your_openai_api_key_here pela sua chave de API da OpenAI.

### 5. Execute a aplicação
```bash
python app.py
```
A aplicação estará disponível em http://localhost:5000/

### Estrutura do Projeto
```bash
.
├── app.py               # Arquivo principal da aplicação Flask
├── templates
│   └── index.html       # Frontend da aplicação (HTML + Tailwind CSS)
├── .env                 # Arquivo contendo as variáveis de ambiente (não deve ser incluído no repositório)
├── requirements.txt     # Lista de dependências do projeto
└── README.md            # Instruções e documentação da aplicação
```

### Dependências
- Flask: Microframework para Python.
- requests: Biblioteca para fazer requisições HTTP.
- python-dotenv: Carrega variáveis de ambiente de um arquivo .env.

### Personalização
Você pode personalizar o conteúdo inicial enviado à API do OpenAI ajustando a mensagem de contexto no arquivo app.py dentro da variável data.

```bash
data = {
    "model": "gpt-4",
    "messages": [
        {"role": "system", "content": "Você é um professor experiente em diversas áreas do conhecimento."},
        {"role": "user", "content": question}
    ],
    "temperature": 0.8,
    "max_tokens": 1000,
    "n": 1
}
```

### Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


### Resumo dos passos:

- **Instalação de dependências**: Clonagem do repositório, criação de ambiente virtual, e instalação dos pacotes listados em `requirements.txt`.
- **Configuração do ambiente**: Criação do arquivo `.env` com as variáveis necessárias.
- **Execução da aplicação**: Comando para iniciar o servidor Flask (`python app.py`).

Esse `README.md` deve cobrir os aspectos essenciais para quem deseja configurar e rodar a aplicação em seu ambiente local.
