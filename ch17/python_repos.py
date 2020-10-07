import json

import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
re = requests.get(url)
print(re.status_code)

response_dict = re.json()
print('Total respositories:', response_dict['total_count'])

repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

print('\nSelected information about each repository:')
with open('github.txt', 'w', encoding='utf-8') as f:
    for repo_dict in repo_dicts:
        f.write('\n\nName:' + repo_dict['name'])
        f.write('\nOwner:' + repo_dict['owner']['login'])
        f.write('\nStars:' + str(repo_dict['stargazers_count']))
        f.write('\nRepository:' + repo_dict['html_url'])
        if 'description' in repo_dict and repo_dict['description'] is not None:
            f.write('\nDescription:' + repo_dict['description'])
