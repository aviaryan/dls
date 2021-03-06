# API

### Getting TEXT from a URL

Send a GET request to `<id>/text`

```sh
> curl http://dls.aviaryan.in/flask/text
abcdeff
hello
world%
```

### Getting FILE from a URL

Using wget or curl, send a request to `<id>/file`

```sh
wget http://dls.aviaryan.in/flask/file -O file.png
```

To have the output file automatically named according to the upload file name, try the following -

```sh
wget --content-disposition http://dls.aviaryan.in/flask/file
```

Using curl,

```sh
curl -J -O http://dls.aviaryan.in/flask/file
```

Source - http://superuser.com/a/301051


### Getting URL status as JSON

Send a GET request to `<id>.json`

```sh
curl http://dls.aviaryan.in/flask.json
```
