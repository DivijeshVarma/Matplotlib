import requests

# Make an API call and store the response.
# we store the URL of the API
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# GitHub is currently on the third version of its API, so we define headers for the API call that ask explicitly
# to use this version
headers = {'Accept': 'application/vnd.github.v3+json'}
# we use requests to make the call to the API
r = requests.get(url, headers=headers)
# we assign the response object to the variable r. The response object has an attribute called status_code,
# which tells us whether the request was successful. (A status code of 200 indicates a successful response.)
print(f'status code: {r.status_code}')
# The API returns the information in JSON format, so we use the json() method to convert the information
# to a Python dictionary z. We store the resulting dictionary in response_dict.
response_dict = r.json()
# process results:
# print(response_dict.keys())
# dict_keys(['total_count', 'incomplete_results', 'items'])

# we print the value associated with 'total_count', which represents the total number of Python repositories on GitHub.
print(f"Total Repositories: {response_dict['total_count']}")

# Explore information about the repositories.
# The value associated with 'items' is a list containing a number of dictionaries, each of which contains data
# about an individual Python repository.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"Keys: {len(repo_dict)}")
# for key in sorted(repo_dict):
#     print(key)

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")