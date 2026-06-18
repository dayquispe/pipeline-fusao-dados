from processamento_dados import Dados

VERDE = "\033[92m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
RESET = "\033[0m"

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#Extract 
print(f"{VERDE}=== ETAPA DE EXTRAÇÃO ==={RESET}")

dados_empresaA = Dados(path_json, 'json')
print(f"{AMARELO}Dados da Empresa A{RESET}")
print(f"{AZUL}Nome das colunas:{RESET} {dados_empresaA.nome_colunas}")
print(f"{AZUL}Qtd de registros nos dados da empresa A:{RESET} {dados_empresaA.qtd_linhas}")

dados_empresaB = Dados(path_csv, 'csv')
print(f"{AMARELO}Dados da Empresa B{RESET}")
print(f"{AZUL}Nome das colunas:{RESET} {dados_empresaB.nome_colunas}")
print(f"{AZUL}Qtd de registros nos dados da empresa B:{RESET} {dados_empresaB.qtd_linhas}")

# Transform 
print(f"\n{VERDE}=== ETAPA DE TRANSFORMAÇÃO ==={RESET}")
# O key_mapping depende de um alinhamento com a equipe de analytics. (Uma regra de negócio)
key_mapping = {'Nome do Item':'Nome do Produto',
               'Classificação do Produto':'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

print(f"{AZUL}Renomeando colunas da empresa B...{RESET}")
dados_empresaB.rename_columns(key_mapping)
print(f"{AZUL}Colunas após renomeação:{RESET} {dados_empresaB.nome_colunas}")

print(f"{AZUL}Realizando fusão dos datasets...{RESET}")
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)

print(f"{AZUL}Nome das colunas após fusão:{RESET} {dados_fusao.nome_colunas}")
print(f"{VERDE}Total de registros após fusão:{RESET} {dados_fusao.qtd_linhas}")

# Load
print(f"\n{VERDE}=== ETAPA DE CARREGAMENTO ==={RESET}")
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f"{VERDE}Arquivo salvo com sucesso em:{RESET} {path_dados_combinados}")

print(f"\n{VERDE}Pipeline executado com sucesso!{RESET}")