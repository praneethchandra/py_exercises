import json
from random_employee import generate_ceo
from random_employee import generate_cto
from random_employee import generate_employee

with open('ceo.json', 'w', encoding='utf8') as json_file:
    json_file.write(generate_ceo())

with open('cto.json', 'w', encoding='utf8') as json_file:
    json_file.write(generate_cto())

for i in range(0,10):
    with open('emp'+str(i)+'.json', 'w', encoding='utf8') as json_file:
        json_file.write(generate_employee())
