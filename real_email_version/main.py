# main.py

from report_generator import gerar_relatorio_por_vendedor
from email_utils import enviar_email_real

if __name__ == "__main__":
    caminho_excel = gerar_relatorio_por_vendedor()
    if caminho_excel:
        caminho_pdf = caminho_excel.replace(".xlsx", ".pdf")
        enviar_email_real(caminho_excel, extra_anexo=caminho_pdf)
