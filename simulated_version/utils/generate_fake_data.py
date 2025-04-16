import pandas as pd
from faker import Faker
import random

fake = Faker('pt_BR')
Faker.seed(42)

vendedores = [fake.first_name() for _ in range(5)]
produtos = ['Motor', 'Compressor', 'Sensor', 'Bomba', 'Painel']
regioes = ['Sul', 'Sudeste', 'Nordeste', 'Norte', 'Centro-Oeste']

dados = []

for _ in range(50):
    dados.append({
        'Data': fake.date_between(start_date='-10d', end_date='today'),
        'Vendedor': random.choice(vendedores),
        'Produto': random.choice(produtos),
        'Valor': round(random.uniform(500, 5000), 2),
        'Região': random.choice(regioes)
    })

df = pd.DataFrame(dados)
df.to_excel('data/vendas.xlsx', index=False)
print("Arquivo vendas.xlsx gerado com sucesso!")
