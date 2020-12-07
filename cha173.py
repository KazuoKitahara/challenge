import re
str="The ghost that says boo haunts the loo"
match = re.findall(".oo",str)
print(match)
