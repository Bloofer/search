import requests
import json
r = requests.get('https://api.github.com/search/issues?q=conflict+label:bug+language:python+state:open&sort=created&order=asc')
if(r.ok):
    repoItem = json.loads(r.text or r.content)
    print json.dumps(repoItem, indent=4, sort_keys=True)
