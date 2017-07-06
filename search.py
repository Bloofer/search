#searching github repositories

import requests
import json

url = 'https://api.github.com/search/'
search_type = 'issues' #commits, issues etc.
query_string = '?q=mergeconflict'
# q : search keywords. able to set keyword with multiple conditions(plain(keyword), repo, language)
# ex) ?q=pep8+repo:ropas/sparrow+language:c

headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url+search_type+query_string, headers=headers)

if(r.ok):
  repoItem = json.loads(r.text or r.content)

  if(repoItem['total_count']==0):
    print 'no result'
  else:
    # [print dump]
    # print json.dumps(repoItem, indent=4, sort_keys=True)

    # [pretty print result]
    print 'Result number : '+str(len(repoItem['items']))+'\n'
    for item in repoItem['items']:
      print ('issue#'+str(item['number'])+' '+item['title']).encode('utf-8')
      
      if (item['closed_at']==None):
        print 'still open'
      else:
        print 'closed at '+str(item['closed_at'])
      
      print item['html_url']

      if (item['comments']==0):
        print 'no comments\n'
      else:
        print str(item['comments'])+' comments'
        com_r = requests.get(item['comments_url'], headers=headers)
        if (com_r.ok):
          comItem = json.loads(com_r.text or com_r.content)
          for com in comItem:
            print (com['user']['login']+' : '+com['body']).encode('utf-8')
          print '\n'
        else:\
          print 'request fail com'
else:
  print 'request fail item'
