import requests
customerURL = "http://api.reimaginebanking.com/customers?key=f6b2994f930f3175da90249976afd314"
merchantURL = 'http://api.reimaginebanking.com/merchants?key=f6b2994f930f3175da90249976afd314'
r1 = requests.get(url=customerURL, params=None)
r2 = requests.get(url=merchantURL, params=None)
data1 = r1.json()
data2 = r2.json()
# for elem in data1:
#     email = elem['last_name']+'@' + elem['first_name'] + '.com'
#     print(email)
#     print(elem['last_name'], elem['first_name'])
for elem in data2:
    name = elem['name'].replace(" ", "")
    email = name+'@email.com'
    print(email, sep='')
#     print(elem['name'])
# print(len(data1))
# print(len(data2))
