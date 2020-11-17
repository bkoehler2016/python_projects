d = {
    'baz': 'hi',
    'Goats': 12,
    'foo': 'bar'

}

d['Beej'] = 33

for k, v in d.items():
    print(f"{k}: {v}")