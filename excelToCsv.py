import pandas as pd

def converter_xlsx_para_csv(arquivo_xlsx, arquivo_csv):
    # Carrega o arquivo Excel (.xlsx) em um DataFrame do pandas
    df = pd.read_excel(arquivo_xlsx , sheet_name='TAB_BRASIL')

    # Escreve o DataFrame em um arquivo CSV
    df.to_csv(arquivo_csv, index=False)

# Exemplo de uso
arquivo_excel = '/home/deluca-ubuntu/products/Coty/Loreal.xlsx'
arquivo_csv = '/home/deluca-ubuntu/products/CotyCSV/Loreal_arquivo.csv'

converter_xlsx_para_csv(arquivo_excel, arquivo_csv)

