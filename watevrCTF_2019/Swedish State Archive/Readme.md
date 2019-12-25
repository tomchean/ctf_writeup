# Swedish State Archive 
---
## Solution
1. First we see in server.py, the "gti" is mis spell
```
from flask import Flask, request, escape
import os
app = Flask("")

@app.route("/")
def index():
    return get("index.html")

@app.route("/<path:path>")
def get(path):
    print("Getting", path)
    if ".." in path:
        return ""

    if "logs" in path or ".gti" in path:
        return "Please do not access the .git-folder"

    if "index" in path:
        path = "index.html"

    if os.path.isfile(path):
        return open(path, "rb").read()

    if os.path.isdir(path):
        return get("folder.html")

    return "404 not found"


if __name__ == "__main__":
    app.run("0.0.0.0", "8000")
```
2.  curl http://13.53.175.227:50000/.git/refs/heads/master and use pigz -d to see the commit content
3. trace the parent commit and we can see a commit whose message is 'did some work on flag.txt' and access the tree, we can see the hash key of flag.txt content.
4. curl the hash key to get the content of flag.txt
