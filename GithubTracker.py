import requests

print("Made By CodePulse")
username = input("Enter GitHub username: ")
repo_url = input("Enter GitHub repository URL: ")

# Extract repository owner and name from URL
repo_url_parts = repo_url.split('/')
repository = repo_url_parts[-1]
owner = repo_url_parts[-2]

# Send HTTP request to GitHub API to retrieve repository information
response = requests.get(f"https://api.github.com/repos/{owner}/{repository}")
if response.status_code == 200:
    repo_info = response.json()
    # Extract information from the repository data
    stars_count = repo_info['stargazers_count']
    description = repo_info['description']
    forks_count = repo_info['forks_count']
    primary_language = repo_info['language']
    created_at = repo_info['created_at']
    updated_at = repo_info['updated_at']
    repo_url = repo_info['html_url']
    homepage_url = repo_info['homepage']
    try:
        license_name = repo_info['license']['name']
    except TypeError:
        license_name = "None"
    # Print the extracted information
    print(f"Repository: {repository}")
    print(f"Description: {description}")
    print(f"Stars: {stars_count}")
    print(f"Forks: {forks_count}")
    print(f"Primary language: {primary_language}")
    print(f"Created at: {created_at}")
    print(f"Last updated: {updated_at}")
    print(f"Repository URL: {repo_url}")
    print(f"Homepage URL: {homepage_url}")
    print(f"License: {license_name}")
else:
    print(f"Unable to retrieve repository information ({response.status_code}).")
