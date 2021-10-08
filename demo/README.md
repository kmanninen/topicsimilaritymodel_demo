# nathan-ice Demo

Demonstrates an implementation of a nathan-ice topic matching scenario. The flow is basically:

1. Retrieve a small set of sample text documents and "train" nathan-ice.
1. Retrieve the text of what is to be matched (aka, the "Agent" text).
1. Retrieve the larger set of unknown documents and insert them into nathan-ice for matching.
1. Execute the nathan-ice matching function and look at the results.

## Prerequisites

* Docker
* A copy of this (nathan-ice) repository

## Installation

```
# From the parent nathan-ice repository
docker-compose up
```

## Execution

This demo runs on an instance of [Jupyter Notebook](https://jupyter.org). To access the notebook, look for the URL on the console that launched the Docker environment. It should appear as something like this:

```
jupyter       |     To access the notebook, open this file in a browser:
jupyter       |         file:///home/jovyan/.local/share/jupyter/runtime/nbserver-16-open.html
jupyter       |     Or copy and paste one of these URLs:
jupyter       |         http://0b90cc578f8a:8888/?token=e04fb77ae092f52dd1a31bdc24d03f79933d0db1f620e77c
jupyter       |      or http://127.0.0.1:8888/?token=e04fb77ae092f52dd1a31bdc24d03f79933d0db1f620e77c
```

Launch the URL from a browser and navigate to the `nathanice_DEMO.ipynb` file.

Run the steps in the file, via the Jupyter Notebook UI.