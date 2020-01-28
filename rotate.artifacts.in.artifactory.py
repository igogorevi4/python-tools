#!/usr/bin/env python

from artifactory import ArtifactoryPath
import datetime

retention_period = 7
# url = "http://repo.jfrog.org/artifactory/gradle-ivy-local"
# put you artifactory path here
url = "https://artifactory.example.com/repo-name"
# put you access token here
api_key = "ExampleApiToken"
today = datetime.datetime.now()


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


rotate_artifacts(url)
