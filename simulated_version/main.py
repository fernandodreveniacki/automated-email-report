# main.py

from report_generator import gerar_relatorio_por_vendedor
from email_utils import simular_envio_email

if __name__ == "__main__":
    caminho_arquivo = gerar_relatorio_por_vendedor()

    if caminho_arquivo:
        print("Relatório pronto para ser enviado por e-mail 🚀")
        simular_envio_email(caminho_arquivo)
