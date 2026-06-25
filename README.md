# Pipeline de Fusão de Dados Empresariais

Projeto desenvolvido para integrar bases de dados de duas empresas após um processo de fusão, aplicando conceitos de ETL (Extract, Transform, Load) e Programação Orientada a Objetos em Python.

## Problema

Após a fusão de duas empresas, cada organização possuía seus dados armazenados em formatos diferentes:

- Empresa A: arquivo JSON
- Empresa B: arquivo CSV

Além disso, as bases utilizavam nomes de colunas diferentes para representar as mesmas informações.

A equipe de Business Intelligence precisava de uma base única e padronizada para realizar análises e construir dashboards.

## Objetivo

Construir um pipeline de dados capaz de:

- Ler arquivos JSON e CSV;
- Padronizar os nomes das colunas;
- Unificar os dados das duas empresas;
- Tratar informações ausentes;
- Gerar uma base consolidada em CSV;
- Permitir reutilização do processo em futuras execuções.

## Estrutura do Projeto

pipeline_dados/

├── data_raw/
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
│
├── data_processed/
│   └── dados_combinados.csv
│
├── notebooks/
│   └── exploracao.ipynb
│
├── scripts/
│   ├── processamento_dados.py
│   └── fusao_mercado_fev.py
│
└── README.md

## Pipeline ETL

### Extract

Leitura automática dos arquivos JSON e CSV através da classe Dados.

### Transform

- Padronização dos nomes das colunas;
- Tratamento de diferenças estruturais;
- Junção dos datasets;
- Tratamento de valores ausentes.

### Load

Geração do arquivo final:

data_processed/dados_combinados.csv

## Conceitos Aplicados

- Python
- Programação Orientada a Objetos (POO)
- Pipeline ETL
- Manipulação de arquivos JSON
- Manipulação de arquivos CSV
- Refatoração de código
- Logs de execução

## Aprendizados

Durante este projeto foram praticados conceitos importantes de Engenharia de Dados, incluindo:

- Leitura de múltiplas fontes de dados;
- Padronização de estruturas heterogêneas;
- Construção de pipelines ETL;
- Refatoração de código procedural para orientação a objetos;
- Aplicação de encapsulamento;
- Organização de projetos Python.