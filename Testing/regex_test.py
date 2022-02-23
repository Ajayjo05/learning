import re

text2= "$******#$%^^ 456, 456, 000 . 00"
pat="(?<=[\W*])(\d*\,\s\d*\,\s\d*\s\.\s\d*)"
match=re.findall(pat, text2)
print(match)

