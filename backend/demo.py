import requests


res = requests.get(
    url= 'https://www.linkedin.com/jobs/search/?currentJobId=3757039507', 
timeout=60)

print(res.text)
