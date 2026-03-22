import pandas as pd
import mysql.connector

# ---------------------------
# CONEXAO COM A BASE DE DADOS
# ---------------------------

conexao = mysql.connector.connect(
    host = 'localhost',
    user = '******',
    password = '******',
    database = 'projeto_vendas'
)

# ------------------------
# LEITURA DA BASE DE DADOS
# ------------------------

df_vendas = pd.read_sql('SELECT * FROM vendas', conexao)
df_produtos = pd.read_sql('SELECT * FROM produtos', conexao)
df_clientes = pd.read_sql('SELECT * FROM clientes', conexao)

# -----------------
# FATURAMENTO TOTAL
# -----------------

faturamento = df_vendas['valor_total'].sum()
print(f'Faturamento total: {faturamento}')

# --------------------
# PRODUTO MAIS VENDIDO
# --------------------

top_produtos = df_vendas.groupby('id_produto')['quantidade'].sum().sort_values(ascending = False)
print(top_produtos)

# ---------------
# VENDAS POR DATA   
# ---------------

df_vendas["data_venda"] = pd.to_datetime(df_vendas["data_venda"])

vendas_por_data = df_vendas.groupby("data_venda")["valor_total"].sum()
print(vendas_por_data)

# ------------
# UNIR TABELAS
# ------------

df_completo = df_vendas.merge(df_produtos, on="id_produto")

top_produtos_nome = df_completo.groupby("nome_produto")["quantidade"].sum().sort_values(ascending=False)

print(top_produtos_nome)
