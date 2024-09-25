#from http.server import SimpleHTTPRequestHandler, HTTPServer

#port = 80
#handler = SimpleHTTPRequestHandler

#with HTTPServer(("", port), handler) as httpd:
#    print(f"Serving on port {port}")
#    httpd.serve_forever()


#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def hello():
#    return "Hello, World! c'est honoré"

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=80)


#from fastapi import FastAPI

#app = FastAPI()

#@app.get("/")
#def read_root():
#    return {"Hello": "World"}

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return f'This page has been viewed {redis.get("hits").decode("utf-8")} times.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

