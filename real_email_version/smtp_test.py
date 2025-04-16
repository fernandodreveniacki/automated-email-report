import smtplib

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    print("✅ Conexão SMTP estabelecida!")
except Exception as e:
    print("❌ Falha na conexão SMTP:", e)
