'''
CamelCase
to 
snake_case
'''
import re
example="HiMyNameIsYerassyl."
x=re.findall('[A-Z][a-z]*',example)
result='_'.join(i.lower() for i in x)
print(result)


