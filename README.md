# DLS

[![Build Status](https://travis-ci.org/aviaryan/dls.svg?branch=master)](https://travis-ci.org/aviaryan/dls)
[![Code Climate](https://codeclimate.com/github/aviaryan/dls/badges/gpa.svg)](https://codeclimate.com/github/aviaryan/dls)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bfa45683aab140a2b40ae51a54baf891)](https://www.codacy.com/app/aviaryan/dls)
[![codecov](https://codecov.io/gh/aviaryan/dls/branch/master/graph/badge.svg)](https://codecov.io/gh/aviaryan/dls)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
[![Launch on OpenShift](http://launch-shifter.rhcloud.com/button.svg)](https://openshift.redhat.com/app/console/application_type/custom?cartridges%5B%5D=python-2.7&initial_git_url=https%3A%2F%2Fgithub.com%2Faviaryan%2Fdls.git&name=dls)

Direct Link Service. A pastebin for text and uploading files where you can choose a custom link. Also file and text will be accessible/downloadable from easy to
remember direct links. http://dls.aviaryan.in/

## Why?

Currently, the options available to quickly share a text or file are pastebin type services which provide a random link after the data is uploaded.
The links are impossible to remember and the only way to retrieve data back from the link is to first store the link somewhere so that it can be recalled.
So I made this service so that anyone can put a paste or upload a file to a url of their choice. Eg >

* [/foraman](http://dls.aviaryan.in/foraman)
* [/networkexam](http://dls.aviaryan.in/networkexam)

Then there are all sorts of ways to fetch information from the url; see [API docs](#api) for them.
Above all, I wanted to take up a sample project to practise Flask so that was it.

**PS** - If you like the idea, please [vote here](https://github.com/aviaryan/dls/issues/15) so that I can make up my mind to buy a short domain.

## Tutorial (Guide)

See the [homepage](http://dls.aviaryan.in/#using)

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
