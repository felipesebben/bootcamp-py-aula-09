from etl import pipeline_calcular_kpi_vendas_consolidado

pasta_entrada : str = "data/raw/"
pasta_saida: str = "data/clean/"
nome_arquivo = "vendas_consolidado"
formato_saida: list = ["csv", "parquet"]

pipeline_calcular_kpi_vendas_consolidado(pasta_entrada, pasta_saida, nome_arquivo, formato_saida)