# Rotation outdated artifact from you Jfrog Artifactiry

Put you artifactory URL to variable `login_url`

``` python
login_url = "https://artifactory.example.com/artifactory"
```

then check if you API path is set to correct value

``` python
api_url = '/api/repositories'
```

put you username and access token to these variables

``` python
username = "USERNAME"
api_key = "PutAccessTokenHere"
```

Before run the `rotate.artifacts.in.artifactory.py` you should install requirements as following:

``` Shell
pip3 install -r requirements.txt --user
```


and then run:

``` Shell
python rotate.artifacts.in.artifactory.py
```
