# \w --> [a-zA-Z0-9À-ú_]
# \w --> [a-zA-Z0-9_] --> re.A
# \W --> [â-zA-Z0-9À-ú_]
# \W --> [â-zA-Z0-9À-ú_] --> re.A
# \d --> [0-9]
# \D --> [^0-9]
# \s --> [\r\n\f\n\t]
# \S --> [^\r\n\f\n\t]
# \b --> borda termina ou começa
# \B --> não borda
#
# 

"""

O que são as flags re.A e re.I

As flags do módulo re em Python, elas modificam o comportamento
 das expressões regulares:

re.I (ou re.IGNORECASE): Faz a correspondência ignorar maiúsculas
 e minúsculas. Por exemplo, re.search(r'abc', 'ABC', re.I) encontrará uma
correspondência.

re.A (ou re.ASCII): Restringe a correspondência a caracteres
 ASCII apenas, ignorando propriedades Unicode. Útil para padrões 
 como \w (que normalmente inclui letras Unicode), tornando-os 
 equivalentes a [a-zA-Z0-9_]. Disponível a partir do Python 3.7.

Essas flags são passadas como terceiro argumento em funções como re.search(), re.findall(), etc. Exemplo: re.findall(r'\w+', texto, re.I | re.A).
"""


import re 

texto = '''
Sim, essa é uma limitação conhecida do Webflow.

Soluções alternativas como duplicação ou JavaScript 
personalizado podem funcionar a curto prazo, mas, à medida 
que a lógica de precificação cresce ou precisa de consistência 
entre os modelos, a manutenção se torna trabalhosa.
54641521656445848548,
Em projetos maiores, as455 equipes geralmente movem essa lógica
 para fora do Webflow (API/camada de dados externa) para que o mesmo 
 bloco de precifica4556ção possa ser reutilizado em todos os lugares sem 
 necessidade de redefinição ou duplicação. fd5451451561

 1956, 56899, 566666

'''

# print(re.findall(r'[a-z]+', texto, flags=re.I))
# print(re.findall(r'[a-zA-Z]+', texto))
# print(re.findall(r'[a-zA-Z0-9]+', texto))
# print(re.findall(r'[a-zA-Z0-9Á-ú]+', texto))
# print(re.findall(r'\w+', texto, flags=re.A))
# print(re.findall(r'\W+', texto, flags=re.A))
# print(re.findall(r'\d+', texto, flags=re.I))
# print(re.findall(r'\D+', texto, flags=re.I))
# print(re.findall(r'\s+', texto, flags=re.I))
# print(re.findall(r'\D+', texto, flags=re.I))
# print(re.findall(r'\be\w+', texto, flags=re.I))
# print(re.findall(r'\w+e\b', texto, flags=re.I))
# print(re.findall(r'\b\w{4}\b', texto, flags=re.I))
print(re.findall(r'\w{4}', texto, flags=re.I))