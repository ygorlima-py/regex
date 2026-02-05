# Meta Caracteres: ^$
# () \1
# () () \1 \2
# (())() \1 \2 \3

import re
from pprint import pprint

texto = '''
<p>Frase 1</p><p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''
# cpf = "454.326.255-08"
# print(re.findall(r'(([0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# tags = re.findall(r'<([dpiv]{1,3})>(?:.+?)<\/\1>', texto)
# tags_named = re.findall(r'<(?P<tag>[dpiv]{1,3})>(?:.+?)<\/(?P=tag)>', texto)

# # pprint(tags)
# pprint(tags_named)

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto))

# for tag in tags:
#     first, second, thirdy = tag
#     print(thirdy)