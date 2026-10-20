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
