import requests

url = 'http://127.0.0.1:5000/results'
r = requests.post(url,json={'Area':5, 'Number_of_bedrooms':200, 'Garden_Surface':400, 'Status':'As new'})

print(r.json())