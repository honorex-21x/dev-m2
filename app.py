#from http.server import SimpleHTTPRequestHandler, HTTPServer

#port = 80
#handler = SimpleHTTPRequestHandler

#with HTTPServer(("", port), handler) as httpd:
#    print(f"Serving on port {port}")
#    httpd.serve_forever()


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! c'est honoré"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

