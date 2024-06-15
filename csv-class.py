import pandas as pd


class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None  # Inicializa o atributo df como None

    def carregar_csv(self):
        self.df = pd.read_csv(
            self.file_path
        )  # Carrega o arquivo CSV para o atributo df

    def filtrar_por(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]


# Exemplo de uso:
arquivo_csv = "./exemplo.csv"
filtro = "estado"
limite = "SP"

arquivo_Csv = CsvProcessor(arquivo_csv)
arquivo_Csv.carregar_csv()
print(arquivo_Csv.filtrar_por(filtro, limite))
