import pandas as pd
from bcb import sgs
import yfinance as yf

start_date = '2018-01-01'
end_date = pd.Timestamp.today().strftime('%Y-%m-%d')

# Dicionário
series_dict = {
    'IPCA': 433,  # IPCA 
    'INPC': 188,  # INPC 
    'ICC': 4393,  # Índice de Confiança do Consumidor 
    'ICI': 7465,  # Índice de Confiança da Indústria 

    'IGPM': 189,  # IGP-M 

    'SELIC': 432,  # Taxa SELIC 

    'Desemprego': 24369,  # Taxa de Desemprego
    'Rendimento_Medio': 22858,  # Rendimento Médio Real 

    'Cambio_USD_BRL': 10813,  # Taxa de Câmbio USD/BRL 
    'Exportacoes': 22701,  # Exportações 
    'Importacoes': 22700,  # Importações 
    'Saldo_Comercial': 24364,  # Saldo Comercial 
    'Reservas_Internacionais': 3546,  # Reservas Internacionais 

    'Divida_Publica': 4513,  # Dívida Pública Bruta (% do PIB) 
    'Resultado_Primario': 4390,  # Resultado Primário do Setor Público (% do PIB) 
    'Juros_Nominais': 13762,  # Juros Nominais do Setor Público (% do PIB) 

    'Producao_Industrial': 21859,  # Produção Industrial 
    'Vendas_Varejo': 1455,  # Índice de Vendas do Varejo 
    'IPP': 28564,  # Índice de Preços ao Produtor 

    'Inadimplencia_PF': 20786,  # Taxa de Inadimplência - Pessoa Física 
    'Credito_Total': 20539,  # Volume de Crédito Total (real)
    
    'Investimento_Estrangeiro': 22701,  # Fluxo de Investimento Estrangeiro em Ações 
    
    'arrecadacao_imposto_renda': 7616,
    
    'emprego_formal': 10802  
}

def fetch_series_data(series_code, start_date, end_date):
    """
    Função para obter e processar dados de uma série específica.
    """
    try:
        series_data = sgs.get(series_code, start=start_date, end=end_date)
        if isinstance(series_data, pd.DataFrame) and series_data.shape[1] > 1:
            series_data = series_data.iloc[:, 0]
        series_data = series_data[~series_data.index.duplicated(keep='first')]
        series_data = series_data.resample('ME').ffill()
        return series_data
    except Exception as e:
        print(f"Erro ao obter a série {series_code}: {e}")
        return pd.Series(dtype='float64')

df = pd.DataFrame()

for serie_name, serie_code in series_dict.items():
    print(f"Coletando dados da série: {serie_name}")
    series_data = fetch_series_data(serie_code, start_date, end_date)
    df[serie_name] = series_data

# usando yfinance
ibovespa = yf.download('^BVSP', start=start_date, end=end_date)
ibovespa_monthly = ibovespa['Adj Close'].resample('ME').last()

df['Ibovespa'] = ibovespa_monthly

# Tratar valores ausentes
df.fillna(method='ffill', inplace=True)
df.fillna(method='bfill', inplace=True)

percent_columns = [
    'IPCA', 'INPC', 'IGPM', 'SELIC', 'Desemprego',
    'Divida_Publica', 'Resultado_Primario', 'Juros_Nominais', 'Inadimplencia_PF'
]

real_columns = [
    'Rendimento_Medio', 'Cambio_USD_BRL', 'Exportacoes', 'Importacoes',
    'Saldo_Comercial', 'Reservas_Internacionais', 'Credito_Total', 'Investimento_Estrangeiro', 'arrecadacao_imposto_renda'
]

absolute_columns = [
    'ICC', 'ICI', 'Producao_Industrial', 'Vendas_Varejo', 'IPP', 'emprego_formal'
]

# Aplicando formatação
df[percent_columns] = df[percent_columns] / 100  
df[real_columns] = df[real_columns].applymap(lambda x: f"R$ {x:,.2f}")
df[absolute_columns] = df[absolute_columns].applymap(lambda x: f"{x:,.2f}")

print(df)

with pd.ExcelWriter('indicadores_economicos.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Dados Economicos')
    
    workbook = writer.book
    worksheet = writer.sheets['Dados Economicos']
    
    percent_format = workbook.add_format({'num_format': '0.00%'})
    
    real_format = workbook.add_format({'num_format': 'R$ #,##0.00'})
    
    absolute_format = workbook.add_format({'num_format': '#,##0.00'})
    
    for col_num, col_name in enumerate(df.columns, 1):
        if col_name in percent_columns:
            worksheet.set_column(col_num, col_num, None, percent_format)
        elif col_name in real_columns:
            worksheet.set_column(col_num, col_num, None, real_format)
        elif col_name in absolute_columns:
            worksheet.set_column(col_num, col_num, None, absolute_format)

print("Arquivo indicadores_economicos.xlsx salvo com sucesso com a formatação adequada.")
