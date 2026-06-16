import json
import csv

from processamento_dados import Dados

def transformando_dados_tabela(dados, nomes_colunas):
    dados_combinados_tabela = [nomes_colunas]

    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indiponivel'))
        dados_combinados_tabela.append(linha)
        
    return dados_combinados_tabela

def salvando_dados(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#Extract 

dados_empresaA = Dados(path_json, 'json')
print(f"Nome das colunas: {dados_empresaA.nome_colunas}")
print(f"Qtd de linhas nos dados da empresa A: {dados_empresaA.qtd_linhas}")

dados_empresaB = Dados(path_csv, 'csv')
print(f"Nome das colunas: {dados_empresaB.nome_colunas}")
print(f"Qtd de linhas nos dados da empresa B: {dados_empresaB.qtd_linhas}")

# Transform 

# O key_mapping depende de um alinhamento com a equipe de analytics. (Uma regra de negócio)
key_mapping = {'Nome do Item':'Nome do Produto',
               'Classificação do Produto':'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)

