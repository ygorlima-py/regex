# Meta Caracteres: ^$ ()
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min , max}
# {10,} 10 ou mais
# {,10} de 0 a 10
# {10} especificamente 10
# {5,10} de 5 a 10
# ()+ {a-zA-Z0-9}
# Quantificadores funcionam para coisas a esquerda dele

import re

texto = '''
O principal ponto de contato para suporte técnico é a Ana Pereira, através do telefone (11) 98765-4321. Para questões administrativas, o contato é o setor financeiro no número 48 3333-1020. Por favor, evitem usar o número antigo, 11987654321, que foi desativado.
Documentação e Arquivos:
O documento principal, com o ID DOC-ALFA-2026-001, foi enviado para revisão. O CPF do gestor responsável é 123.456.789-00 e o CNPJ da empresa parceira é 98.765.432/0001-10. Todos os arquivos de referência podem ser encontrados no nosso portal interno, acessível em https://projetos.nossa-empresa.com/alfa/documentos. Para referências externas, consultamos o site http://www.exemplo.org.
Próximos Passos:
A próxima entrega está agendada para 15-03-2026. O status atual do sistema pode ser verificado em tempo real através da nossa API. O sistema apresentou um erro inesperado (código 500 - Internal Server Error ) às 16:45:30, mas a equipe de TI já foi acionada. O chamado de suporte é o CH-9876-B. O endereço de IP do servidor de testes é 192.168.1.100.
maria , joão, João foi pra casa do caralho com Maria
joooooooooooooooooãooooooooooooo, mudando de linha
Veeemm veeem veem vem
'''

print(re.findall(r'jo+ão+',  texto, flags=re.I))
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

# print(re.sub(r'jo+ão+',  "Felipe", texto, flags=re.I))

