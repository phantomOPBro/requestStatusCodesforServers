import requests
a="10.1.33."
for i in range(68,85):
  try:
    r=requests.get("http://"+str(a)+str(i))
    print(str(r.status_code) + " " + i)
  except requests.exceptions.RequestException as e:
    continue
