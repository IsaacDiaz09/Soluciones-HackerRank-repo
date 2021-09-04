import re

Regex_Pattern = r'^[123][120][sx0][30|Aa][xs|u][\.|\,]$'	# Do not delete 'r'.
"""
Longitud de: 6
Primer caracter: 1, 2 o 3
Segundo caracter: 1, 2 o 0
Tercer caracter: x, s o 0
Cuarto caracter: 3, 0 , A o a
Quinto caracter: x, s o u
Sexto caracter: . o ,
"""
print(str(bool(re.search(Regex_Pattern, input()))).lower())
