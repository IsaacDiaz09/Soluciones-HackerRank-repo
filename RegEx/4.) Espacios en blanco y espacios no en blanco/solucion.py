import re

# busca el siguiente patron:
# - dos caracteres que no son espacio en blanco, dos que si, dos caracteres que 
# no son espacio en blanco y debe acabar con dos espacios en blanco

Regex_Pattern = r"^[\S]{2}\s[\S]{2}\s[\S]{2}$"	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())