# Projeto OFX - Leitura de Extrato e PostgreSQL

Aplicação Python para leitura de ficheiros bancários `.ofx`, exibição de totais e armazenamento em banco de dados PostgreSQL.

## Funcionalidades
- Leitura e parsing de extratos bancários `.ofx`
- Resumo financeiro (entradas, saídas e saldo)
- Inserção no PostgreSQL com tratamento antiduplicação (`ON CONFLICT`)
- Proteção de credenciais com variáveis de ambiente (`.env`)

## Tecnologias
- Python 3
- PostgreSQL / DBeaver
- `ofxparse`, `psycopg2-binary`, `python-dotenv`

## Como Executar o Projeto

 **Clonar o repositório:**
   ```bash
   git clone [https://github.com/A-Mrts23/ProjetoOFX.git](https://github.com/A-Mrts23/ProjetoOFX.git)
   cd ProjetoOFX
```
## Criar e ativar o ambiente virtual:
```
python -m venv venv
.\venv\Scripts\activate
``` 
## Instalar as dependências:
```
pip install ofxparse psycopg2-binary python-dotenv
```
## Configurar as variáveis de ambiente:
```
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

## Executar a aplicação: 
```
python main.py
```
