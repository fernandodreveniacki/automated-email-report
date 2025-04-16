# 📊 Projeto de Automação de Relatórios por E-mail com Python

Este projeto demonstra como automatizar a geração e o envio de relatórios diários utilizando Python. Ele possui **duas versões**:

- 🔄 **Versão Simulada**: executa todo o fluxo, mas **não envia o e-mail de verdade** (apenas simula).
- 📬 **Versão Real**: envia o relatório **realmente por e-mail**, utilizando o Gmail via SMTP com senha de aplicativo.

---

## 🗂️ Estrutura Geral do Projeto

```
AUTOMATED_REPORT/
├── real_email_version/
│   ├── data/                  # Entrada (Excel)
│   ├── logs/                  # Logs de execução
│   ├── reports/               # Relatórios gerados (Excel + PDF)
│   ├── utils/                 # Módulos auxiliares
│   ├── .env                   # Variáveis sensíveis (não subir)
│   ├── config.template.env    # Modelo do .env
│   ├── config.py              # Leitura das variáveis do .env
│   ├── email_utils.py         # Envio real com SMTP
│   ├── logger_utils.py        # Registro de logs
│   ├── main.py                # Execução manual
│   ├── report_generator.py    # Geração dos relatórios
│   ├── scheduler.py           # Agendamento automático
│   ├── smtp_test.py           # Teste de conexão SMTP
│   └── test_email_sender.py   # Teste de envio individual
│
├── simulated_version/
│   ├── data/                  # Entrada de dados simulados
│   ├── logs/                  # Logs simulados
│   ├── reports/               # Relatórios gerados
│   ├── utils/                 # Módulos auxiliares
│   ├── config.py              # Configuração hardcoded
│   ├── email_utils.py         # Simulação de envio
│   ├── logger_utils.py        # Log local
│   ├── main.py                # Execução principal simulada
│   ├── report_generator.py    # Geração de relatórios
│   └── scheduler.py           # Agendamento simulado
│
├── .gitignore                 # Ignora arquivos sensíveis
├── config_template.env        # Modelo para configurar o .env
├── README.md                  # Este arquivo
└── requirements.txt           # Dependências do projeto
```

---

## 🔄 Como usar a Versão Simulada

1. Gere os dados:
```bash
cd simulated_version
python generate_fake_data.py
```

2. Execute o fluxo:
```bash
python main.py
```

> 📌 Sempre execute **de dentro da pasta `simulated_version/`** para que os caminhos relativos funcionem corretamente.

---

## 📬 Como usar a Versão Real com Envio

1. Configure seu `.env` com base em `config_template.env`
2. Gere os dados:
```bash
cd real_email_version
python generate_fake_data.py
```

3. Execute o fluxo:
```bash
python main.py
```

4. (Opcional) Agende execuções diárias:
```bash
python scheduler.py
```

> 📌 Sempre execute **de dentro da pasta `real_email_version/`** para evitar erros ao acessar arquivos.

---

## 🔐 Segurança

- As variáveis sensíveis estão em `.env` e **não devem ser versionadas**
- O projeto inclui um `.gitignore` que protege esses dados
- O `config_template.env` serve de referência para qualquer novo desenvolvedor

---

## 📝 Funcionalidades Comuns

- 📊 Geração de relatórios (.xlsx e .pdf)
- 📧 Envio (real ou simulado)
- 🪵 Logs salvos em `logs/logs.txt`
- 📅 Agendamento diário com `schedule`

---

## 👨‍💻 Autor

Desenvolvido por Fernando — para portfólio e estudos.

