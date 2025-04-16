# email_utils.py

from email.message import EmailMessage
from datetime import datetime
import os
from logger_utils import registrar_log

def simular_envio_email(arquivo_relatorio, destinatario="destinatario@exemplo.com"):
    data_hoje = datetime.now().strftime('%d/%m/%Y')
    msg = EmailMessage()
    msg['Subject'] = f"Relatório Diário de Vendas - {data_hoje}"
    msg['From'] = "relatorio.automacao@empresa.com"
    msg['To'] = destinatario

    corpo = f"""
    Olá!

    Segue em anexo o relatório diário de vendas do dia {data_hoje}.

    Atenciosamente,
    Sistema de Automação de Relatórios
    """
    msg.set_content(corpo)

    if os.path.exists(arquivo_relatorio):
        with open(arquivo_relatorio, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(arquivo_relatorio)

        msg.add_attachment(file_data,
                           maintype='application',
                           subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                           filename=file_name)

        print("✅ E-mail montado com sucesso!")
        registrar_log(f"📬 E-mail simulado com anexo: {file_name} para {destinatario}")
    else:
        msg = "❌ Arquivo de relatório não encontrado. E-mail não montado."
        print(msg)
        registrar_log(msg)

        
    # Simulação do envio (exibir dados)
    print("📬 SIMULAÇÃO DE ENVIO")
    print(f"De: {msg['From']}")
    print(f"Para: {msg['To']}")
    print(f"Assunto: {msg['Subject']}")
    print("Corpo:")
    print(corpo)
    print(f"Anexo: {file_name}")
    print("⚠️ E-mail não enviado de verdade (modo simulado).")
