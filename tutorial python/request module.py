import requests

r = requests.get("https://site.financialmodelingprep.com/")

print(r.text)

print(r.status_code)

# url = "www.something.com"
# data = {
#     "pi": 4,
#     "p2": 8

# }

# r2 = requests.post(url= url, data= data)