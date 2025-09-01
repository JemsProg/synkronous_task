import requests

def get_github_status():
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        return "GitHub API is up! ✅"
    else:
        return f"Something’s wrong! Status: {response.status_code}"

if __name__ == "__main__":
    print(get_github_status())
