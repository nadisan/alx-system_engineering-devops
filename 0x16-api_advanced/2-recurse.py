#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import json
import requests
import sys



def recurse(subreddit, host_list=[], after="null"):
    """
    Fundtion queries reddit API
    Returns top 10 hotspots
    else 0
    """
    username = 'ledbag123'
    password = 'Reddit72'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}

    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers

    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        list_titles = r.json()['data']['children']
        for a in list_titles[:10]:
            print(a['data']['title'])
    else:
        return(print("None"))
