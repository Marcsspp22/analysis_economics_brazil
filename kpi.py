import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QTextBrowser, QLabel

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig)

def create_chart(chart_type):
    sc = MplCanvas(window, width=5, height=4, dpi=100)
    
    sc.ax.axvline(pd.Timestamp('2021-03-01'), color='red', linestyle='--', linewidth=1, label='Pico da Pandemia')
    sc.ax.axvline(pd.Timestamp('2020-02-01'), color='black', linestyle='--', linewidth=1, label='Inicio da Pandemia')


    if chart_type == "Inflação: IPCA e INPC":
        sc.ax.plot(df.index, df['IPCA'], marker='o', label='IPCA (%)', color='red')
        sc.ax.plot(df.index, df['INPC'], marker='o', label='INPC (%)', color='orange')
        sc.ax.set_title('Inflação: IPCA e INPC (2018-2024)', fontsize=14)
        sc.ax.set_xlabel('Data', fontsize=12)
        sc.ax.set_ylabel('Inflação (%)', fontsize=12)
        sc.ax.legend(loc='upper left')
        explanation = "O IPCA é o índice oficial de inflação no Brasil, enquanto o INPC reflete o custo de vida para famílias com renda entre 1 e 5 salários mínimos."
        
    elif chart_type == "Taxa SELIC e Dívida Pública":
        sc.ax.plot(df.index, df['SELIC'], marker='o', label='SELIC (%)', color='blue')
        sc.ax.set_ylabel('SELIC (%)', fontsize=12, color='blue')
        sc.ax.tick_params(axis='y', labelcolor='blue')
        
        ax2 = sc.ax.twinx()
        ax2.plot(df.index, df['Divida_Publica'], marker='o', label='Dívida Pública (% do PIB)', color='green')
        ax2.set_ylabel('Dívida Pública (% do PIB)', fontsize=12, color='green')
        ax2.tick_params(axis='y', labelcolor='green')
        
        sc.ax.set_title('Taxa SELIC e Dívida Pública (2018-2024)', fontsize=14)
        sc.ax.set_xlabel('Data', fontsize=12)
        sc.ax.legend(loc='upper left')
        ax2.legend(loc='upper right')
        explanation = "A SELIC é a taxa básica de juros da economia, usada para controlar a inflação. A dívida pública em relação ao PIB indica a saúde fiscal do país."
        
    elif chart_type == "Produção Industrial":
        sc.ax.plot(df.index, df['Producao_Industrial'], marker='o', color='purple', label='Produção Industrial')
        sc.ax.set_title('Produção Industrial (2018-2024)', fontsize=14)
        sc.ax.set_xlabel('Data', fontsize=12)
        sc.ax.set_ylabel('Índice (Base 100)', fontsize=12)
        sc.ax.legend(loc='upper left')
        explanation = "Este gráfico mostra a evolução da Produção Industrial, refletindo a atividade econômica no setor secundário."
        
    elif chart_type == "Desemprego":
        sc.ax.plot(df.index, df['Desemprego'], marker='o', label='Taxa de Desemprego (%)', color='darkred')
        sc.ax.set_title('Taxa de Desemprego (2018-2024)', fontsize=14)
        sc.ax.set_xlabel('Data', fontsize=12)
        sc.ax.set_ylabel('Porcentagem (%)', fontsize=12)
        sc.ax.legend(loc='upper left')
        explanation = "Este gráfico mostra a evolução da Taxa de Desemprego ao longo do tempo, refletindo as condições do mercado de trabalho."
        
    elif chart_type == "Variação do Dólar (USD/BRL)":
        sc.ax.plot(df.index, df['Cambio_USD_BRL'], marker='o', label='Dólar (USD/BRL)', color='blue')
        sc.ax.set_title('Variação do Dólar (USD/BRL) (2018-2024)', fontsize=14)
        sc.ax.set_xlabel('Data', fontsize=12)
        sc.ax.set_ylabel('Cotação (R$)', fontsize=12)
        sc.ax.legend(loc='upper left')
        explanation = "A variação do dólar reflete a volatilidade cambial e o impacto de fatores internos e externos sobre a economia brasileira."
        
    elif chart_type == "Variação do Ibovespa":
        sc.ax.plot(df.index, df['Ibovespa'], marker='o', label='Ibovespa', color='green')
        sc.ax.set_title('Variação do Ibovespa (2018-2024)', fontsize=14)
        sc.ax.set_xlabel('Data', fontsize=12)
        sc.ax.set_ylabel('Pontos', fontsize=12)
        sc.ax.legend(loc='upper left')
        explanation = "O Ibovespa é o principal índice da Bolsa de Valores brasileira, refletindo o desempenho das ações mais negociadas."
    
    elif chart_type == "Inadimplência":
        sc.ax.plot(df.index, df['Inadimplencia_PF'], marker='o', label='Inadimplência PF (%)', color='red')
        sc.ax.set_title('Inadimplência (2018-2024)', fontsize=14)
        sc.ax.set_xlabel('Data', fontsize=12)
        sc.ax.set_ylabel('Inadimplência (%)', fontsize=12, color='red')
        sc.ax.legend(loc='upper left')
        sc.ax.tick_params(axis='y', labelcolor='red')
        explanation = "Este gráfico mostra a evolução da inadimplência das pessoas físicas ao longo do tempo. Ele reflete as dificuldades dos consumidores em cumprir suas obrigações financeiras, o que pode indicar problemas econômicos mais amplos."
        
    elif chart_type == "Dívida Pública vs. Resultado Primário":
        sc.ax.plot(df.index, df['Divida_Publica'], marker='o', label='Dívida Pública (% do PIB)', color='green')
        sc.ax.set_ylabel('Dívida Pública (% do PIB)', fontsize=12, color='green')
        sc.ax.tick_params(axis='y', labelcolor='green')
        
        ax2 = sc.ax.twinx()
        ax2.plot(df.index, df['Resultado_Primario'], marker='o', label='Resultado Primário (% do PIB)', color='blue')
        ax2.set_ylabel('Resultado Primário (% do PIB)', fontsize=12, color='blue')
        ax2.tick_params(axis='y', labelcolor='blue')
        
        sc.ax.set_title('Dívida Pública vs. Resultado Primário (2018-2024)', fontsize=14)
        sc.ax.set_xlabel('Data', fontsize=12)
        sc.ax.legend(loc='upper left')
        ax2.legend(loc='upper right')
        explanation = "Este gráfico compara a Dívida Pública e o Resultado Primário utilizando dois eixos y, oferecendo uma visão clara sobre a sustentabilidade fiscal do país."

    return sc, explanation

# Carregar os dados do arquivo Excel
file_path = 'indicadores_economicos.xlsx'
df = pd.read_excel(file_path, sheet_name='Dados Economicos', index_col=0)

# Remover o símbolo "R$" e converter para float nas colunas monetárias
monetary_columns = [ 'Rendimento_Medio', 'Cambio_USD_BRL', 'Exportacoes',
                    'Importacoes', 'Saldo_Comercial', 'Reservas_Internacionais', 'Credito_Total']
df[monetary_columns] = df[monetary_columns].replace('[R$ ,]', '', regex=True).astype(float)

# Ajustar os dados percentuais para exibição
percent_columns = [
    'IPCA', 'INPC', 'IGPM', 'SELIC', 'Desemprego',
    'Divida_Publica', 'Resultado_Primario', 'Juros_Nominais', 'Inadimplencia_PF'
]
df[percent_columns] *= 100  # Convertendo para porcentagem

# Criação da aplicação PyQt5
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Dashboard Econômico do Brasil (2018-2024)')
window.setGeometry(100, 100, 1200, 1000)  # Definir a resolução da janela

layout = QGridLayout()

# Definir os gráficos a serem criados
charts = [
    "Inflação: IPCA e INPC", 
    "Taxa SELIC e Dívida Pública", 
    "Produção Industrial", 
    "Desemprego", 
    "Variação do Dólar (USD/BRL)",
    "Variação do Ibovespa", 
    "Inadimplência", 
    "Dívida Pública vs. Resultado Primário"
]

# Adicionar gráficos e explicações ao layout
row, col = 0, 0
for i, chart in enumerate(charts):
    sc, explanation = create_chart(chart)
    layout.addWidget(sc, row, col)
    
    text_browser = QTextBrowser()
    text_browser.setPlainText(explanation)
    text_browser.setMaximumHeight(50)  # Limitar a altura da explicação
    layout.addWidget(text_browser, row + 1, col)
    
    col += 1
    if col > 1:
        col = 0
        row += 2

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
