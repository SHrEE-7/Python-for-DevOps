import requests
res = requests.get("https://api.github.com/users/SHrEE-7/repos")
my_repos = res.json()
print(my_repos[0])

# for repository in my_repos:
#     print(f"Repository Name:{repository['name']} --> Repository URL:{repository['url']}")