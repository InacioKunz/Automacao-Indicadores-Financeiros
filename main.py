import os
import requests
import pandas as pd
import smtplib
import ssl
from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

response = requests.get('http://127.0.0.1:8000/api/painel/relatorio')

dados = response.json()  # pega o conteúdo JSON como dicionário Python

def formatar_data(texto):
    for formato in ('%Y-%m-%d %H:%M:%S.%f', '%d/%m/%Y'):
        try:
            return datetime.strptime(texto, formato).strftime('%d/%m/%Y')
        except ValueError:
            continue
    return texto

def montar_linha(nome, lista, chave_valor, chave_data):
    item = lista[-1]  # pega o último item da lista (funciona pra 1 ou vários itens)
    return {
        'indicador': nome,
        'valor': item[chave_valor],
        'data': formatar_data(item[chave_data]),
    }

linhas = []
linhas.append(montar_linha('Dólar', dados['dolar'], 'cotacaoCompra', 'dataHoraCotacao'))
linhas.append(montar_linha('Euro', dados['euro'], 'cotacaoCompra', 'dataHoraCotacao'))
linhas.append(montar_linha('Selic', dados['selic'], 'valor', 'data'))
linhas.append(montar_linha('IPCA', dados['ipca'], 'valor', 'data'))

indicadores = pd.DataFrame(linhas)
indicadores.to_excel('indicadores.xlsx', index=False)

servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
contexto = ssl.create_default_context()
servidor_email.starttls(context=contexto)
servidor_email.login(os.getenv('EMAIL_REMETENTE'), os.getenv('EMAIL_SENHA_APP'))

remetente = os.getenv('EMAIL_REMETENTE')
destinatarios = [os.getenv('EMAIL_DESTINATARIO')]

mensagem = EmailMessage()
mensagem['Subject'] = "Indicadores"
mensagem['From'] = remetente
mensagem['To'] = ', '.join(destinatarios)
mensagem.set_content('Olá, indicadores financeiros.')

with open('indicadores.xlsx', 'rb') as arquivo:
    conteudo = arquivo.read()

mensagem.add_attachment(
    conteudo,
    maintype='application',
    subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    filename='indicadores.xlsx'
)

servidor_email.send_message(mensagem)
servidor_email.quit()