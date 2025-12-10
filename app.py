import os
import pandas as pd
import plotly.express as px

caminho = "C:\\Users\\felip\\Downloads\\Vendas-20251209T130024Z-3-001\\Vendas"
lista_arquivos = os.listdir(caminho)
tabela_total = pd.DataFrame()

for arquivo in lista_arquivos:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"C:\\Users\\felip\\Downloads\\Vendas-20251209T130024Z-3-001\\Vendas\\{arquivo}")

        tabela_total = pd.concat([tabela_total, tabela])

# Calculando o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produtos)

# Calculando o produto que mais faturou (em faturamento)
tabela_total ['Faturamento'] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Quantidade Vendida", "Faturamento"]].sort_values(by="Faturamento",ascending=False)
print(tabela_faturamento)

# Calculando a loja/cidade que mais vendeu (em faturamento)
tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(tabela_lojas)


# Criando o gráfico
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento")
grafico.show()