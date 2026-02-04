# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] Conjunto de caractere

import re

texto = '''
O principal ponto de contato para suporte técnico é a Ana Pereira, através do telefone (11) 98765-4321. Para questões administrativas, o contato é o setor financeiro no número 48 3333-1020. Por favor, evitem usar o número antigo, 11987654321, que foi desativado.
Documentação e Arquivos:
O documento principal, com o ID DOC-ALFA-2026-001, foi enviado para revisão. O CPF do gestor responsável é 123.456.789-00 e o CNPJ da empresa parceira é 98.765.432/0001-10. Todos os arquivos de referência podem ser encontrados no nosso portal interno, acessível em https://projetos.nossa-empresa.com/alfa/documentos. Para referências externas, consultamos o site http://www.exemplo.org.
Próximos Passos:
A próxima entrega está agendada para 15-03-2026. O status atual do sistema pode ser verificado em tempo real através da nossa API. O sistema apresentou um erro inesperado (código 500 - Internal Server Error ) às 16:45:30, mas a equipe de TI já foi acionada. O chamado de suporte é o CH-9876-B. O endereço de IP do servidor de testes é 192.168.1.100.
maria , joão, João foi pra casa do caralho com Maria

'''

print(re.findall(r'documentacao|enviado|st.t',  texto))
print(re.findall(r'[Dd]ocumentação|enviado|st.t',  texto))
print(re.findall(r'[Pp]róxima|enviado|st.t',  texto))
print(re.findall(r'próxim[a-z]|enviado|st.t',  texto))
print(re.findall(r'próxim[a-z]|enviado|st.t',  texto))
print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão',  texto))
print(re.findall(r'jOãO|mAriA',  texto, flags=re.I))
