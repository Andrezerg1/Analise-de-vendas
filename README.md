# Projeto de Análise de Vendas com Python, SQL e Power BI

## Visão Geral

Este projeto tem como objetivo simular um ambiente real de análise de dados, desenvolvendo um pipeline completo que envolve geração, armazenamento, tratamento e visualização de dados de vendas.

A solução permite analisar indicadores estratégicos como faturamento, ticket médio e desempenho de produtos e regiões.

---

## Tecnologias Utilizadas

- Python (pandas, geração de dados)
- MySQL (armazenamento e modelagem)
- Power BI (visualização e dashboard)

---

## ⚙️ Etapas do Projeto

### 1.  Geração de Dados (Python)
- Script responsável por criar dados fictícios de clientes, produtos e vendas
- Geração de 1000 registros de vendas com valores aleatórios
- Exportação em arquivos `.csv`

---

### 2. Modelagem de Dados (SQL)
- Criação do banco de dados `projeto_vendas`
- Estruturação de tabelas:
  - `clientes`
  - `produtos`
  - `vendas`
- Definição de chaves primárias e estrangeiras

---

### 3. Importação de Dados
- Importação dos arquivos CSV para o MySQL
- Validação da integridade dos dados

---

### 4. Análise e Métricas
- Conexão do Python com o banco de dados
- Cálculo de indicadores principais:
  - Faturamento total
  - Ticket médio
  - Volume de vendas

---

### 5. Dashboard (Power BI)
- Construção de visualizações interativas:
  - Faturamento ao longo do tempo
  - Produtos mais vendidos
  - Vendas por cidade
- Criação de KPIs:
  - Faturamento total
  - Ticket médio
  - Total de vendas

---

## 📌 Principais Insights

- Produtos de maior valor agregado possuem maior impacto no faturamento
- Existe variação nas vendas ao longo do tempo
- Distribuição geográfica das vendas permite identificar regiões com maior potencial

---

## Objetivo do Projeto

Demonstrar habilidades práticas em:
- Manipulação e análise de dados
- Modelagem de banco de dados
- Construção de dashboards
- Integração entre ferramentas de dados

---

## Possíveis Melhorias

- Automação da atualização dos dados
- Uso de dados reais
- Criação de novos KPIs (crescimento, margem, etc.)
- Deploy do dashboard no Power BI Service

---

## 📎 Autor

### André Zerger Bigaran
- Desenvolvedor Back-End e Analista de Dados Junior.
