import os
import psycopg2
from dotenv import load_dotenv
from ofxparse import OfxParser

# Carrega as variáveis de ambiente salvas no arquivo .env
load_dotenv()

# Configurações obtidas com segurança a partir do .env
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

# 1. Leitura do arquivo OFX
with open("extrato.ofx", "rb") as arquivo:
    ofx = OfxParser.parse(arquivo)

entradas = 0.0
saidas = 0.0
total_movimentacoes = 0

print("=" * 45)
print("          EXTRATO BANCÁRIO DETALHADO          ")
print("=" * 45)

# 2. Conectando ao PostgreSQL
try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    banco_conectado = True
    print("[OK] Conectado ao PostgreSQL com sucesso!")
except Exception as e:
    print(f"\n[ERRO] Falha ao conectar ao PostgreSQL: {e}\n")
    banco_conectado = False

novos_inseridos = 0
duplicados_ignorados = 0

# 3. Percorrendo as movimentações do OFX
for t in ofx.account.statement.transactions:
    total_movimentacoes += 1
    valor = float(t.amount)

    if valor > 0:
        entradas += valor
    else:
        saidas += valor

    # Exibição individual da movimentação
    print(f"Data      : {t.date.strftime('%d/%m/%Y')}")
    print(f"Valor     : R$ {valor:10.2f}")
    print(f"Descrição : {t.memo}")
    print("-" * 45)

    # 4. Gravação no PostgreSQL (Desafio Extra)
    if banco_conectado:
        sql = """
            INSERT INTO movimentacoes (data_movimentacao, valor, descricao)
            VALUES (%s, %s, %s)
            ON CONFLICT (data_movimentacao, valor, descricao) DO NOTHING;
        """
        cursor.execute(sql, (t.date.strftime('%Y-%m-%d'), valor, t.memo))
        
        if cursor.rowcount > 0:
            novos_inseridos += 1
        else:
            duplicados_ignorados += 1

# Confirmar alterações e fechar conexão
if banco_conectado:
    conn.commit()
    cursor.close()
    conn.close()

# 5. Resumo da Atividade Prática
saldo = entradas + saidas

print("\n" + "=" * 45)
print("                 RESUMO DA CONTA             ")
print("=" * 45)
print(f"Quantidade total de movimentações : {total_movimentacoes}")
print(f"Total de Entradas                : R$ {entradas:10.2f}")
print(f"Total de Saídas                  : R$ {abs(saidas):10.2f}")
print(f"Saldo Calculado                  : R$ {saldo:10.2f}")
print("=" * 45)

if banco_conectado:
    print(f"Registros gravados no banco      : {novos_inseridos}")
    print(f"Registros duplicados ignorados  : {duplicados_ignorados}")
    print("=" * 45)