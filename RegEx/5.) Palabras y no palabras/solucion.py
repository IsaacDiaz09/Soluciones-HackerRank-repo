import re
# el patron busca que tenga tres caracteres alfanumericos, un no alfanumerico seguido de 10 alfanumericos,
# otro caracter no alfanumerico y debe terminar con 3 alfanumericos 
Regex_Pattern = r"[\w]{3}\W[\w]{10}\W[\w]{3}$"	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
