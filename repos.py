import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()

#print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

#examnine first repo
#repo_dict = repo_dicts[0]

print("\nSelected information for each repo:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars', repo_dict['stargazers_count'])
    print('Repo:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
    
