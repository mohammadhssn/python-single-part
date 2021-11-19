# from urllib.request import urlopen
# import json
#
# url = "http://api.exchangeratesapi.io/v1/latest?access_key=201675638656066ccced978ca1ebf227&symbols=USD,AUD,CAD,PLN,MXN&format=1"
#
# with urlopen(url) as a:
#     #data = json.load(a)
#     data = a.read()
#
# pdata = json.loads(data)
#
# print(pdata)
#
# with open("api-test.json", "w") as f:
#     json.dump(pdata, f, indent=2)