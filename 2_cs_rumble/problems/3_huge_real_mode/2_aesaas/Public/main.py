import http.server
from socketserver import ThreadingMixIn
from subprocess import run



class ApiHandler(http.server.BaseHTTPRequestHandler):
    
    def read_body(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len)
        return body
    


    def __init__(self, cmd):
        content = self.read_body()

        output = run(
            cmd,
            capture_output=True,
            input=content, 
            shell=True
        ).stdout

        self.send_response(200)
        self.end_headers()
        self.wfile.write(output)


obj = ApiHandler(cmd="echo \"hey\"")