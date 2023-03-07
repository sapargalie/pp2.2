#CamelCase
#snake_case
example='hello_i_am_lenovo'
import re
def snake_to_camel(example):
    example1=example.split('_') #['hello', 'i', 'am', 'lenovo']
    return ''.join(i.capitalize() for i in example1)
print(snake_to_camel(example))
