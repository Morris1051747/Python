import requests
url = 'https://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-000157-002'
r = requests.get(url)

bigBox = r.json()['result']['records']

for data in bigBox:
    print(data)






