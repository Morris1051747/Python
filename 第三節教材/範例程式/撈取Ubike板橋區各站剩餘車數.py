import requests

url = 'https://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=json'

r = requests.get(url,verify=False)

sites = r.json()

for s in sites:
    if s["sarea"] == "板橋區":
        print('%s 可借車位數：%s 台'%(s['sna'],s['sbi']))


