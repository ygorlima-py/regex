import re

text = "O API da xAI cobra por uso (ex: ~$0.20 por milhão de tokens input + image fees), sem free tier permanente em 2026. Teve um beta com $25/mês free até fim"

regexp = re.compile(r'API')

print(regexp.search(text))
print(regexp.findall(text))
print(regexp.sub("api",  text))
