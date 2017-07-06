#searching github repositories

import requests
import json

url = 'https://api.github.com/search/'
search_type = 'issues' #commits, issues etc.
query_string = '?q=mergeconflict'
# q : search keywords. able to set keyword with multiple conditions(plain(keyword), repo, language)
# ex) ?q=pep8+repo:ropas/sparrow+language:c
# sort : sort field (stars, forks, updated) / order : sort order (asc, desc)
# ex) ?q=conflict&sort=stars&order=desc

headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url+search_type+query_string, headers=headers)

if(r.ok):
    repoItem = json.loads(r.text or r.content)
#   print json.dumps(repoItem, indent=4, sort_keys=True)
    for item in repoItem['items']:
      print 'issue#'+str(item['number'])+' '+item['title']
      print item['html_url']+'\n'

else:
    print 'request fail'
