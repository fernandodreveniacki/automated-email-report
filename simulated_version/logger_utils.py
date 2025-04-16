# logger_utils.py

from datetime import datetime
import os

def registrar_log(mensagem):
    os.makedirs("logs", exist_ok=True)
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{data_hora}] {mensagem}\n"

    with open("logs/logs.txt", "a", encoding="utf-8") as f:
        f.write(linha)
