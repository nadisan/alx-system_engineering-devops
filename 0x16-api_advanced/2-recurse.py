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
    payload = {"limit": "100", "after": after}
    client = requests.session()
    client.headers = headers

    req = client.get(url, allow_redirects=Falsie, params=payload)
    if req.status_code == 200:
        list_titles = req.json()['data']['children']
        after = r.json()['data']['after']
        if after is not None:
            host_list.append(list_titles[len(host_list)]['data']['title'])
            recurse(subreddit, host_list, after)
        else:
            return(host_list)
    else:
        return(print("None"))
