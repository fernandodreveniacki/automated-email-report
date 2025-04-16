# test_email_send.py
import smtplib
from email.message import EmailMessage

EMAIL_SENDER = "seu_email@gmail.com"
EMAIL_PASSWORD = "sua_senha_de_aplicativo"
EMAIL_RECEIVER = ["destino1@gmail.com"]


msg = EmailMessage()
msg["Subject"] = "Teste simples de e-mail"
msg["From"] = EMAIL_SENDER
msg["To"] = ", ".join(EMAIL_RECEIVER)
msg.set_content("Este é um teste simples de envio real por Python + Gmail.")

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print("✅ E-mail enviado com sucesso!")
except Exception as e:
    print("❌ Erro no envio:", e)
