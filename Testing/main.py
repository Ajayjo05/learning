import re
text = "Final Fantasy XIII-2 is a 2011 role-playing video game developed and published by Square Enix. XIII-2 is a direct sequel to the 2009 role-playing game Final Fantasy XIII and part of the Fabula Nova Crystallis subseries. Development of the game began in early 2010 and involved many of the key designers from the previous game. It includes modified features from the previous game, including fast-paced combat and a customizable Paradigm system. XIII-5, XIII-3"
pattern="(?i)(xiii\-)+([1234])"
match=re.findall(pattern, text)
print(match)

text1="i was born on july 5.lalit was born on august 14. Mukesh was born on july 25. gagan was born on june 14."
pattern1="(?i)(on)\s([a-z]*)\s(\d*)" #(?i)(?<=(on))\s\w+\s(\d*) (<--with positive look behind) or (?i)(on)\s\w+\s(\d*)
match1 = re.findall(pattern1, text1)
print(match1)

text1="i was born on july 5.lalit was born on august 14. Mukesh was born on july 25. gagan was born on june 14."
pattern1="(?i)(?<=(on))\s\w+\s(\d*)"
match1 = re.findall(pattern1, text1)
print(match1)

text1="i was born on july 5.lalit was born on august 14. Mukesh was born on july 25. gagan was born on june 14."
pattern1="(?i)(on)\s\w+\s(\d*)"
match1 = re.findall(pattern1, text1)
print(match1)