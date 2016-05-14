# API

### Getting TEXT from a URL

Send a GET request to `<id>/text`

```sh
curl http://dlus.herokuapp.com/flask/text
abcdeff
hello
world%
```

### Getting FILE from a URL

Using wget or curl, send a request to `<id>/file`

```sh
wget http://dlus.herokuapp.com/flask/file -O file.png
```

To have the output file automatically named according to the upload file name, try the following -

```sh
wget --content-disposition http://dlus.herokuapp.com/flask/file
```

Using curl,

```sh
curl -J -O http://dlus.herokuapp.com/flask/file
```

Source - http://superuser.com/a/301051