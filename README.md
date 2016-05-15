# DLS

Direct Link Service. A pastebin for text and uploading files where you can choose a custom link. Also file and text will be accessible/downloadable from easy to 
remember direct links. http://dlus.herokuapp.com/ 

```
http://bit.do/dlus
http://bit.ly/dlus000
http://bit.do/dlus000
https://is.gd/dlus000
```

## Why?

Currently, the options available to quickly share a text or file are pastebin type services which provide a random link after the data is uploaded. 
The links are impossible to remember and the only way to retrieve data back from the link is to first store the link somewhere so that it can be recalled. 
So I made this service so that anyone can put a paste or upload a file to a url of their choice. Eg >

* [/foraman](http://dlus.herokuapp.com/foraman)
* [/networkexam](http://dlus.herokuapp.com/networkexam)

Then there are all sorts of ways to fetch information from the url; see [API docs](#api) for them.
Above all, I wanted to take up a sample project to practise Flask so that was it.
**PS** - If you like the idea, please [vote here](https://github.com/aviaryan/dls/issues/15) so that I can make up my mind to buy a short domain.

## Technologies used

* Python 2.7
* Flask
* SQLAlchemy (and Alembic)

## Setup (Deployment)

See the [setup instructions](docs/SETUP.md)

## API

See API [docs](docs/API.md).

## Testing

```bash
python -m unittest discover tests
# or
nosetests
```
