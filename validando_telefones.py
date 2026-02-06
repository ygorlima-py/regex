import re 

# link: https://regex101.com/r/63JMGd/1

regex = re.compile(r"^(?:\(\d{2}\)\s)(?:9\s)(?:\d{4}-\d{4})$", flags=re.M)


texto = ("(27) 9 9308-8893\n"
	"(81)98394-2967\n"
	"(62)     98964-6398\n"
	"(92) 9476-8150\n"
	"99424-5180\n\n")


for telefone in regex.findall(texto):
    print(telefone)

