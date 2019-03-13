import requests
import sqlite3

def import_gists_to_database(db, username, commit=True):
    url = 'https://api.github.com/users/{username}/gists'.format(username=username)
    response = requests.get(url)
    list_of_gists = response.json()
    query = """INSERT INTO gists (github_id,html_url,git_pull_url,git_push_url,commits_url,
                forks_url,public,created_at,updated_at,comments,comments_url) 
                VALUES (?,?,?,?,?,?,?,?,?,?,?)"""
    for gist in list_of_gists:
        db.execute(query, [gist['id'],gist['html_url'],
                gist['git_pull_url'],gist['git_push_url'],gist['commits_url'],
                gist['forks_url'],gist['public'],gist['created_at'],gist['updated_at'],
                gist['comments'],gist['comments_url']])
    if commit == True:
        db.commit()
