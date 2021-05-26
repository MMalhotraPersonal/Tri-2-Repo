from github import Github

git_instance = Github(login_or_token="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", base_url="https://api.github.com")
user = git_instance.get_user()
login = user.login
print(user)
repo = user.get_repo("Tri-2-Repo")
repo.edit(allow_rebase_merge=False)
