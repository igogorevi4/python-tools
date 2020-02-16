To run simple python-web-app you need to clone this repo:

```shell
git clone https://github.com/igogorevi4/python-tools.git
```

Go to directory:
```shell
cd cd python-tools/simple-python-web-server-in-k8s/
```

And run starting shell-script:
```shell
run.service.sh
```

When cluster is installed and set, you can check your service using these commands:
```shell
curl --data "6" http://127.0.0.1/factorial
curl http://127.0.0.1/
curl http://127.0.0.1/ping
```

If you don't need this service anymore you can destoy it and clean with the script:
```shell
./clean.up.sh
```
