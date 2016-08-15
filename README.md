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

`zookeeper_hosts` can either be a list of strings `["example-01", "example-02"]` or a
string of comma separated values `"example-01,example-02"`.
