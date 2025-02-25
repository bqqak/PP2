import re

with open('row.txt', 'r', encoding='utf-8') as r:
    file = r.read()
#1
pattern = re.findall(r'ab*', file)
print(pattern)
#2
pattern = re.findall(r'ab{2, 3}', file)
print(pattern)
#3
pattern = re.findall(r'\b[a-z]+_[a-z]+\b', file)
print(pattern)
#4
pattern = re.findall(r"[A-Z]+[a-z]+", file)
print(pattern)
#5
pattern = re.findall(r"a.+b", file)
print(pattern)
#6
text_to_replace = "Hello, world. This is a test."
something = re.sub(r"[ ,\.]", ':',text_to_replace)
print(something)
#7

def replace_match(match):
    return match.group(1).upper()
def snake_to_camel(snake_str):
    return re.sub(r'_([a-z])', replace_match, snake_str)
snake_string = "hello_world_this_is_python"
camel_case_string = snake_to_camel(snake_string)
print(camel_case_string)

#8

text_to_match = "HelloWorldPythonRegex"
pattern = r"[A-Z]"
result = re.split(pattern, text_to_match)
print(result)

#9

text_to_match = "HelloWorldPythonRegex"
pattern = r"[A-Z]"
result = re.split(pattern, text_to_match)
print(result)

#10
def camel_to_snake(camel_str):
    snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()
    return snake_str

camel_string = "helloWorldPythonRegex"
snake_case_string = camel_to_snake(camel_string)

print(snake_case_string)