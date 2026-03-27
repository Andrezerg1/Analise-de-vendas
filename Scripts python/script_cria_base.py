import pandas as pd
import random
from datetime import datetime, timedelta

# ----------------------
#       CLIENTES       
# ----------------------

clientes = []
cidades = ['São paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']

for i in range(1,51):
    clientes.append({
        "id_cliente": i,
        "nome": f"Cliente {i}",
        "cidade": random.choice(cidades)
    })

df_clientes = pd.DataFrame(clientes)

# -------------------------
# PRODUTOS
# -------------------------

produtos = [
    {"id_produto": 1, "nome_produto": "Notebook", "categoria": "Eletrônicos", "preco": 3500},
    {"id_produto": 2, "nome_produto": "Mouse", "categoria": "Eletrônicos", "preco": 80},
    {"id_produto": 3, "nome_produto": "Teclado", "categoria": "Eletrônicos", "preco": 150},
    {"id_produto": 4, "nome_produto": "Monitor", "categoria": "Eletrônicos", "preco": 900},
    {"id_produto": 5, "nome_produto": "Cadeira", "categoria": "Móveis", "preco": 600},
    {"id_produto": 6, "nome_produto": "Mesa", "categoria": "Móveis", "preco": 1200},
]

df_produtos = pd.DataFrame(produtos)

# -------------------------
# VENDAS
# -------------------------

vendas = []
data_inicial = datetime(2023, 1, 1)

for i in range(1, 1001):
    data = data_inicial + timedelta(days=random.randint(0, 365))
    produto = random.choice(produtos)
    quantidade = random.randint(1, 5)
    valor_total = quantidade * produto["preco"]

    vendas.append({
        "id_venda": i,
        "data": data.strftime("%Y-%m-%d"),
        "id_cliente": random.randint(1, 50),
        "id_produto": produto["id_produto"],
        "quantidade": quantidade,
        "valor_total": valor_total
    })

df_vendas = pd.DataFrame(vendas)

# -------------------------
# SALVAR CSV
# -------------------------

df_clientes.to_csv("clientes.csv", index=False)
df_produtos.to_csv("produtos.csv", index=False)
df_vendas.to_csv("vendas.csv", index=False)

print("Arquivos gerados com sucesso!")