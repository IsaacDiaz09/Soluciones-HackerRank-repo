import re

# Empareja con el formato nnn.nnn.nnn.nnn donde (.) se debe escribir con el caracter de escape
regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"	# Do not delete 'r'.

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())