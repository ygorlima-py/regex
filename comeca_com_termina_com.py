# Metacaracteres:
# ^ --> Começa com
# $ --> Termina Com
# [^a-z] --> Negação


import re


cpf = "454.326.255-08"
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9-]+', cpf))