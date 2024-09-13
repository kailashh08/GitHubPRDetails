import requests
import pandas as pd

owner = 'TAMU-STAT-624-Spring-2024'
repo = 'mad-libs-with-git-and-github-group_17_stat_624'
 
url = f'https://api.github.com/repos/{owner}/{repo}/pulls?state=all'
#print(url)

response = requests.get(url)
pull_requests = response.json()
#print(pull_requests)

pull_data = []

for pr in pull_requests:
    pull_data.append({
        'PR Number': pr['number'],
        'Title': pr['title'],
        'User': pr['user']['login'],
        'Status': pr['state'],
        'Message': pr['body'],
        'Created at': pr['created_at'],
        'Closed at': pr['closed_at'],
        'Merged at': pr['merged_at'],
        'Auto-merge': pr['auto_merge'],
        'Requested Reviewer': pr['requested_reviewers'][0]['login'] if pr['requested_reviewers'] else None
    })

Pull_request_df = pd.DataFrame(pull_data)

print(Pull_request_df.head(10))
Pull_request_df.to_csv('pull_requests_data.csv', index=False)

# for pr in pull_requests:
#     print(f"PR Number: {pr['number']}, Title: {pr['title']}, User: {pr['user']['login']}, Status: {pr['state']}, Message: {pr['body']},\
#     Created at: {pr['created_at']}, Closed at: {pr['closed_at']}, Merged at: {pr['merged_at']}, Auto-merge: {pr['auto_merge']},\
#     Requested Reviewer: {pr['requested_reviewers'][0]['login']}")


### For Later - 


# curl -L \
#   -H "Accept: application/vnd.github+json" \
#   -H "Authorization: Bearer <Token>" \
#   -H "X-GitHub-Api-Version: 2022-11-28" \
#   https://api.github.com/repos/TAMU-STAT-624-Spring-2024/mad-libs-with-git-and-github-group_17_stat_624/pulls/1/reviews


# review_data = []
# for pnum in range(len(Pull_request_df)):
#     PRNum = Pull_request_df['PR Number'][pnum]
#     url2 = f'https://api.github.com/repos/{owner}/{repo}/pulls/{PRNum}/reviews?state=all'
#     print(url2)
#     response_reviews = requests.get(url2)
#     reviews = response_reviews.json()
#     print(reviews)

#     '''review_data.append({
#         'PR Number': 
#     })'''