# https://www.hackerrank.com/challenges/excluding-specific-characters/problem?isFullScreen=true
import re
"""
First caracter should not be a digit
Second caracter should not be a lowercase vowel
Third caracter should not be b, c, D or F.
Fourth caracter should not be a whitespace caracter ( \r, \n, \t, \f or <space> ).
Fifth caracter should not be a uppercase vowel
Sixth caracter should not be a . or , symbol.
"""
Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'	# Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
