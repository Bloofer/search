#searching sparrow issues

import requests
import json

url = 'https://api.github.com/search/issues?q=repo:ropas/sparrow'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)

if(r.ok):
    repoItem = json.loads(r.text or r.content)
    #print json.dumps(repoItem, indent=4, sort_keys=True)
    for item in repoItem['items']:
      print 'issue#'+str(item['number'])+' '+item['title']
      print item['html_url']+'\n'

else:
    print 'request fail'
