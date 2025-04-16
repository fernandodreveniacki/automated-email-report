# scheduler.py

import schedule
import time
from report_generator import gerar_relatorio_por_vendedor
from email_utils import simular_envio_email
from logger_utils import registrar_log

def tarefa_diaria():
    registrar_log("Iniciando tarefa agendada")
    caminho_arquivo = gerar_relatorio_por_vendedor()

    if caminho_arquivo:
        simular_envio_email(caminho_arquivo)
        registrar_log("✅ Tarefa finalizada com sucesso.")
    else:
        registrar_log("⚠️ Tarefa falhou ao gerar relatório.")

# Agendar para rodar diariamente às 08:00
schedule.every().day.at("11:47").do(tarefa_diaria)

print("⏱️ Agendador iniciado! Esperando a hora da execução...")

# Loop contínuo
while True:
    schedule.run_pending()
    time.sleep(1)
