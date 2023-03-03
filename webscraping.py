import requests
r = requests.get('https://stackoverflow.com/questions/tagged/python')
print(r)
print(r.content)
