# runners
A Python lib to provide wrappers around common runnable patterns.


## Lock Helper

```
$ python
>>> import runners
>>> with runners.lock("/foo/bar", zookeeper_hosts=["example-01", "example-02"]):
...     # Do something exclusively
...     pass
... 
```

Zookeeper hosts can also be passed in via an environment variable.

```
$ export ZOOKEEPER_HOSTS='example-01,example-02'
$ python
>>> import runners
>>> with runners.lock("/foo/bar"):
...     # Do something exclusively
...     pass
... 
```
