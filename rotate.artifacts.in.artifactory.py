#!/usr/bin/env python

from artifactory import ArtifactoryPath
import datetime

retention_period = 7
# put you artifactory path here
# url = "http://repo.jfrog.org/artifactory/gradle-ivy-local"
url = "https://artifactory.example.com/repo-name"
today = datetime.datetime.now()


def get_age_of_artifact(artifact_url):
    properties = ArtifactoryPath.stat(artifact_url)
    creation_date = properties.ctime
    # removing timezone
    creation_date = creation_date.replace(tzinfo=None)
    aritfact_age = today - creation_date
    return aritfact_age.days


def delete_artifact(artifact_url):
    url = ArtifactoryPath(artifact_url)
    if url.exists():
        url.unlink()


def get_artifacts_urls(artifactory):
    path = ArtifactoryPath(artifactory)
    return path


def rotate_artifacts(artifactory_url):
    for artifact_url in get_artifacts_urls(artifactory_url):
        artifactory_age = int(get_age_of_artifact(artifact_url))
        if artifactory_age > retention_period:
            print("Deleting the artirfact: {0}; artifact age: {1} ".format(artifact_url,artifactory_age))
            delete_artifact(artifact_url)


rotate_artifacts(url)
