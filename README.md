Automação de Relatório de Indicadores Econômicos

Script em Python que consome o endpoint JSON de um painel de indicadores econômicos em Laravel (dólar, euro, Selic e IPCA), gera um relatório em Excel e envia por e-mail automaticamente.

A ideia do projeto é simular um fluxo típico de automação de rotina: uma fonte de dados expõe uma API, e um robô/script externo consome essa API, processa os dados e distribui o resultado — o mesmo padrão usado em automações com UiPath ou Power Automate, aqui implementado em Python.

O que o script faz
Faz uma requisição HTTP para o endpoint /api/painel/relatorio da aplicação Laravel.
Organiza os indicadores recebidos (dólar, euro, Selic, IPCA) em uma tabela.
Gera um arquivo Excel (.xlsx) com os dados.
Envia um e-mail com o relatório em anexo via SMTP.
Tecnologias
Python
requests — consumo da API
pandas + openpyxl — geração do relatório em Excel
smtplib / email — envio de e-mail com anexo
Como rodar
bash
pip install requests pandas openpyxl

Antes de executar, configure as credenciais de e-mail como variáveis de ambiente (nunca diretamente no código):

bash
# .env ou variáveis de ambiente
EMAIL_REMETENTE=seu_email@gmail.com
EMAIL_SENHA_APP=sua_senha_de_app
EMAIL_DESTINATARIO=destinatario@gmail.com

O envio usa uma senha de app do Gmail, não a senha normal da conta — é necessário ter a verificação em duas etapas ativada.

bash
python main.py
Relação com o projeto em Laravel

Este script depende da aplicação Laravel estar rodando e expondo o endpoint /api/painel/relatorio. Os dois projetos fazem parte do mesmo exercício: o Laravel atua como fonte de dados (API), e este script atua como consumidor/automação — reproduzindo, em menor escala, o tipo de integração entre sistemas que ferramentas de RPA fazem no dia a dia.

O que o script faz
Faz uma requisição HTTP para o endpoint /api/painel/relatorio da aplicação Laravel.
Organiza os indicadores recebidos (dólar, euro, Selic, IPCA) em uma tabela.
Gera um arquivo Excel (.xlsx) com os dados.
Envia um e-mail com o relatório em anexo via SMTP.
Tecnologias
Python
requests — consumo da API
pandas + openpyxl — geração do relatório em Excel
smtplib / email — envio de e-mail com anexo
Como rodar
bash
pip install requests pandas openpyxl

Antes de executar, configure as credenciais de e-mail como variáveis de ambiente (nunca diretamente no código):

bash
# .env ou variáveis de ambiente
EMAIL_REMETENTE=seu_email@gmail.com
EMAIL_SENHA_APP=sua_senha_de_app
EMAIL_DESTINATARIO=destinatario@gmail.com

O envio usa uma senha de app do Gmail, não a senha normal da conta — é necessário ter a verificação em duas etapas ativada.

bash
python main.py
Relação com o projeto em Laravel

Este script depende da aplicação Laravel estar rodando e expondo o endpoint /api/painel/relatorio. Os dois projetos fazem parte do mesmo exercício: o Laravel atua como fonte de dados (API), e este script atua como consumidor/automação — reproduzindo, em menor escala, o tipo de integração entre sistemas que ferramentas de RPA fazem no dia a dia.

<img width="317" height="212" alt="{71EB4E82-9B19-4F58-8EBC-488EC9B440E8}" src="https://github.com/user-attachments/assets/5a45a6b5-c50d-4b88-bb20-e1e0907e069d" />

<img width="611" height="476" alt="image" src="https://github.com/user-attachments/assets/d6146392-f0c8-4397-b015-011e07e9d088" />

