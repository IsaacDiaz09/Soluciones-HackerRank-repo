import re

# EL patron define que debe iniciar con un digito, le sigan cuatro caracteres alfanumericos y termine con un punto (.)
Regex_Pattern = r"^\d[\w]{4}\.$"	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
