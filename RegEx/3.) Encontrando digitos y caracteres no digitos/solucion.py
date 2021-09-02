import re

# Busca el siguiente patron: 
# dos digitos seguidos de un no digito, dos digitos y un no digito, y para finalizar 4 digitos o mas
Regex_Pattern = r"^[\d]{2}\D[\d]{2}\D[\d]{4,}$"	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())