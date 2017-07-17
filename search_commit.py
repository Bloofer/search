#searching github repositories

from __future__ import print_function
import requests
import json

rnum = 0
inum = 100

while(inum>=100):
    inum = 0
    rnum += 1
    url = 'https://api.github.com/search/'
    search_type = 'commits' #commits, issues etc.
    query_string = '?q=merge bug+Language:c+page='+str(rnum)+'&per_page=100'
    # q : search keywords. able to set keyword with multiple conditions(plain(keyword), repo, language, pages(default:30))
    # ex) ?q=pep8+repo:ropas/sparrow+language:c+page=2&per_page=100

    headers = {'Accept': 'application/vnd.github.cloak-preview'}
    r = requests.get(url+search_type+query_string, headers=headers)

    rst_file = open('result/result'+str(rnum)+'.html','wt')
    print ('<!DOCTYPE html>', file = rst_file)
    print ('<html lang="en"><head><meta charset="UTF-8">', file = rst_file)
    print ('<meta name="viewport" content="width=device-width, initial-scale=1.0">', file = rst_file)
    print ('<meta http-equiv="X-UA-Compatible" content="ie=edge">', file = rst_file)
    print ('<title>Result page #'+str(rnum)+'</title></head><body>', file = rst_file)

    if(r.ok):
      repoItem = json.loads(r.text or r.content)

      if(repoItem['total_count']==0):
        print ('no result', file = rst_file)
      else:
        # [print dump]
        # print json.dumps(repoItem, indent=4, sort_keys=True)

        # [pretty print result]
        inum = len(repoItem['items'])
        print ('Result number : '+str(inum)+'<br>', file = rst_file)
        for item in repoItem['items']:
          print (('committer id : '+item['commit']['author']['name']).encode('utf-8'), file = rst_file)
          # print (('commit log : '+item['commit']['message']).encode('utf-8'), file = rst_file)
          # log is hidden b.c. of many lines
          print (('commit date : '+str(item['commit']['committer']['date'])).encode('utf-8'), file = rst_file)
          print ('<a href="'+item['html_url']+'">commit link</a>', file = rst_file)
          if (item['commit']['comment_count']==0):
            print ('no comments<br>', file = rst_file)
          else:
            print (str(item['comments']['comment_count'])+' comments', file = rst_file)
            com_r = requests.get(item['comments_url'], headers=headers)
            if (com_r.ok):
              comItem = json.loads(com_r.text or com_r.content)
              for com in comItem:
                print ((com['user']['login']+' : '+com['body']).encode('utf-8'), file = rst_file)
              print ('<br>', file = rst_file)
            else:
              print ('request fail com', file = rst_file)
    else:
      print ('request fail item', file = rst_file)

    print ('</body></html>', file = rst_file)
