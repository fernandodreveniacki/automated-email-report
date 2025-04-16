# report_generator.py

import pandas as pd
from datetime import datetime
import os
from logger_utils import registrar_log
from fpdf import FPDF

def gerar_relatorio_por_vendedor():
    os.makedirs("reports", exist_ok=True)

    try:
        df = pd.read_excel("data/vendas.xlsx")
    except FileNotFoundError:
        msg = "❌ Arquivo 'vendas.xlsx' não encontrado."
        print(msg)
        registrar_log(msg)
        return None

    relatorio = df.groupby('Vendedor')['Valor'].sum().reset_index()
    relatorio = relatorio.sort_values(by='Valor', ascending=False)

    data_hoje = datetime.now().strftime('%Y-%m-%d')
    nome_excel = f"reports/relatorio_{data_hoje}.xlsx"
    nome_pdf = f"reports/relatorio_{data_hoje}.pdf"

    # Excel
    relatorio.to_excel(nome_excel, index=False)
    registrar_log(f"✅ Relatório Excel gerado: {nome_excel}")
    
    print(f"📊 Excel salvo com sucesso: {nome_excel}")


    # PDF
    salvar_pdf_do_relatorio(relatorio, nome_pdf)
    registrar_log(f"📄 Relatório PDF gerado: {nome_pdf}")

    return nome_excel 

def salvar_pdf_do_relatorio(df, nome_arquivo_pdf):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Relatório de Vendas por Vendedor", ln=True, align='C')
    pdf.ln(10)

    # Cabeçalhos
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, "Vendedor", 1)
    pdf.cell(50, 10, "Total em R$", 1)
    pdf.ln()

    # Dados
    pdf.set_font("Arial", '', 12)
    for index, row in df.iterrows():
        pdf.cell(100, 10, str(row["Vendedor"]), 1)
        pdf.cell(50, 10, f'{row["Valor"]:.2f}', 1)
        pdf.ln()

    pdf.output(nome_arquivo_pdf)
    print(f"📄 PDF salvo com sucesso: {nome_arquivo_pdf}")