import os
import json
import utils.git_functions

# Get GitHub environment variables
github_token = os.getenv('GITHUB_TOKEN')
event_path = os.getenv('GITHUB_EVENT_PATH')

# Load event details (JSON) of the pull request
with open(event_path, 'r') as f:
    event = json.load(f)

    comment = {
        "body": "Adding a comment"
    }

# Post the comment on the PR
    pr_comment_response = utils.git_functions.post_comment_to_pull_request(event, github_token, comment)

    if pr_comment_response.status_code != 201:
        print(f"Failed to add comment. Status code: {pr_comment_response.status_code}")
        print(pr_comment_response.json())
    else:
        print("Comment added successfully!")

