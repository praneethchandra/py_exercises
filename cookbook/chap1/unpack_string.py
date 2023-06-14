line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print(f'line: {line}, uname: {uname}, fields: {fields}, homedir: {homedir}, sh: {sh}')


record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

print(f'record: {record}, name: {name}, year: {year}')