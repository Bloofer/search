#searching github repositories

import requests
import json

url = 'https://api.github.com/search/'
search_type = 'commits' #commits, issues etc.
query_string = '?q=semantic error'
# q : search keywords. able to set keyword with multiple conditions(plain(keyword), repo, language)
# ex) ?q=pep8+repo:ropas/sparrow+language:c

headers = {'Accept': 'application/vnd.github.cloak-preview'}

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
      print ('committer id : '+item['commit']['author']['name']).encode('utf-8')
      print ('commit log : '+item['commit']['message']).encode('utf-8')
      print ('commit date : '+str(item['commit']['committer']['date'])).encode('utf-8')
      print item['html_url']
      if (item['commit']['comment_count']==0):
        print 'no comments\n'
      else:
        print str(item['comments']['comment_count'])+' comments'
        com_r = requests.get(item['comments_url'], headers=headers)
        if (com_r.ok):
          comItem = json.loads(com_r.text or com_r.content)
          for com in comItem:
            print (com['user']['login']+' : '+com['body']).encode('utf-8')
          print '\n'
        else:
          print 'request fail com'
else:
  print 'request fail item'
