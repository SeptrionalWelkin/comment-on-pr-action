import requests


def get_pull_request_metadata(event):
    repo = event['repository']['full_name']
    pr_number = event['pull_request']['number']

    return repo, pr_number


# Adds a comment to a pull request
def post_comment_to_pull_request(event, github_token, comment):
    # Extract PR information
    repo, pr_number = get_pull_request_metadata(event)

    # GitHub API URL to comment on a PR
    comment_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    # Headers for Github request to post the comment on the PR
    comment_headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    pr_comment_response = requests.post(comment_url, headers=comment_headers, json=comment)

    return pr_comment_response
