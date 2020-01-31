#!/usr/bin/env python

from artifactory import ArtifactoryPath
# import artifactory
import datetime
import requests
import json

retention_period = 7

# put you artifactory path here
login_url = "https://artifactory.example.com/artifactory"

api_url = '/api/repositories'
url = login_url + api_url

# put you username and access token here
username = "USERNAME"
api_key = "PutAccessTokenHere"

payload = {'inUserName': username, 'inUserPass': api_key}
today = datetime.datetime.now()


def get_repos_list():
    with requests.Session() as session:
        p = session.post(login_url, data=payload)
        j = session.get(url).text
        json_content = json.loads(j)
        repositories = []
        for i in json_content:
            for key, value in i.items():
                if key == "url":
                    repositories.append(value)
        return repositories


def get_latest_version_age(artifact_url):
    path = ArtifactoryPath(artifact_url, apikey=api_key)
    properties = ArtifactoryPath.stat(path)
    modification_date = properties.mtime
    # removing timezone
    modification_date = modification_date.replace(tzinfo=None)
    aritfact_age = today - modification_date
    return aritfact_age.days


def delete_artifact(artifact_url):
    url = ArtifactoryPath(artifact_url, apikey=api_key)
    if url.exists():
        url.unlink()


def get_artifacts_urls(artifactory):
    path = ArtifactoryPath(artifactory, apikey=api_key)
    return path


def rotate_artifacts(artifactory_url):
    for artifact_url in get_artifacts_urls(artifactory_url):
        artifactory_age = int(get_latest_version_age(artifact_url))
        if artifactory_age > retention_period:
            print("Deleting the artirfact: {0}; artifact age: {1} ".format(artifact_url,artifactory_age))
            delete_artifact(artifact_url)


def main():
    repos = get_repos_list()
    for artifactory_url in repos:
        rotate_artifacts(artifactory_url)


main()

