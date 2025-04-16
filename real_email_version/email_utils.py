# email_utils.py

import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
from logger_utils import registrar_log
from config import EMAIL_PASSWORD, EMAIL_RECEIVER, EMAIL_SENDER, SMTP_SERVER, SMTP_PORT


def enviar_email_real(arquivo_anexo, extra_anexo=None):
    data_hoje = datetime.now().strftime('%d/%m/%Y')

    msg = EmailMessage()
    msg['Subject'] = f"Relatório de Vendas - {data_hoje}"
    msg['From'] = EMAIL_SENDER
    msg['To'] = ", ".join(EMAIL_RECEIVER)

    corpo = f"""
    Olá,

    Segue em anexo o relatório de vendas do dia {data_hoje}.

    Atenciosamente,
    Sistema de Automação
    """
    msg.set_content(corpo)

    if os.path.exists(arquivo_anexo):
        with open(arquivo_anexo, 'rb') as f:
            msg.add_attachment(f.read(),
                maintype='application',
                subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                filename=os.path.basename(arquivo_anexo)
            )


    if extra_anexo and os.path.exists(extra_anexo):
        with open(extra_anexo, 'rb') as f:
            msg.add_attachment(f.read(),
                maintype='application',
                subtype='pdf',
                filename=os.path.basename(extra_anexo)
            )

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("✅ E-mail enviado com sucesso!")
        registrar_log(f"📨 E-mail real enviado para: {EMAIL_RECEIVER}")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")
        registrar_log(f"❌ Falha ao enviar e-mail real: {str(e)}")
