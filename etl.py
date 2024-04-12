import pandas as pd
import os
import glob

# Funcao de extract que le e consolida arquivos .json

def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    """
    Extrai dados em formato json de diretorio apontado. Retorna DataFrame do Pandas

    Args:
    
    - `pasta` (str) - diretorio do conjunto de dados a ser extraido
    
    Returns:
    
    - `pd.DataFrame`
    """
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# Funcao que transforma os dados, retornando kpi

def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria indicador `Total` de valor total vendido, baseado em `df["Quantidade"]` * `df["Vendas"]` 

    Args:
    
    - `df` (`pd.DataFrame`) - DataFrame de entrada da trasnformacao
    
    Returns:
    
    - `pd.DataFrame`
    """    
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


def carregar_dados(df: pd.DataFrame, pasta_saida: str, nome_arquivo: str, formato_saida: list):
    """
    Carrega os dados transformados no diretorio apontado. Permite saida em `.csv` ou `.parquet`

    Args:
    
    - `df` (`pd.DataFrame`) - DataFrame de entrada a ser carregado
    - `pasta_saida` (str) - Diretorio de saida dos dados carregados
    - `formato_saida` (list) - Formato de saida a ser escolhido (`.csv` ou `.parquet`)
    
    Returns:
    
    - `None`
    """   
    for formato in formato_saida:
        if formato == "csv":
            df.to_csv(f"{pasta_saida}{nome_arquivo}.csv", index=False)
        if formato == "parquet":
            df.to_parquet(f"{pasta_saida}{nome_arquivo}.parquet", index=False)


def criar_pasta_saida(path_pasta:str):
    """
    Cria diretorio de saida caso nao exista.

    Args:

    `path_pasta` (str) - Diretorio de saida dos dados carregados.

    Returns:

    `None`
    """
    if not os.path.exists(path_pasta):
        os.makedirs(path_pasta)


def pipeline_calcular_kpi_vendas_consolidado(pasta_entrada: str, pasta_saida: str, nome_arquivo: str, formato_saida: list):
    """
    Executa o ETL completo da aplicacao. Carrega os dados concatenados, 
    cria KPI de vendas e carrega os dados consolidados no formato e diretorio desejados.

    Args:

    `pasta_entrada` (str) - Diretorio de entrada dos dados a serem ingeridos
    `pasta_saida` (str) - Diretorio de saida dos dados transformados
    `nome_arquivo` (str) - Nome do arquivo de saida
    `formato_saida` (list) - Formato de saida dos dados transformados


    Returns:

    `None`
    """    
    data_frame = extrair_dados_e_consolidar(pasta_entrada)
    data_frame_calculado = calcular_kpi_total_vendas(data_frame)
    criar_pasta_saida(pasta_saida)
    carregar_dados(data_frame_calculado, pasta_saida, nome_arquivo, formato_saida)