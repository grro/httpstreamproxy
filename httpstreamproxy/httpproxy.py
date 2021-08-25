from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
from socketserver import ThreadingMixIn
import uuid
import requests



class Connection:

    def __init__(self, client_address):
        self.id = str(uuid.uuid4())
        self.creation_date = datetime.now()
        self.client_address = client_address

    def __hash__(self):
        return self.id.__hash__()

    def __str__(self):
        return self.creation_date.isoformat() + " " +  str(self.client_address[0]) + ":" + str(self.client_address[1])

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.creation_date < other.creation_date

    def __eq__(self, other):
        return self.creation_date == other.creation_date


class RequestHandler(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        self.server = server
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_GET(self):
        connection = Connection(self.client_address)
        self.server.on_connected(connection)
        try:
            resp = requests.get(self.server.target_url, stream=True, verify=self.server.verify)
            self.send_response(200)
            self.send_header('Content-type', resp.headers['Content-Type'])
            self.end_headers()

            for chunk in resp.iter_content(chunk_size=10 * 1024):
                self.wfile.write(chunk)
        except Exception as e:
            print(e)
        finally:
            self.server.on_disconnected(connection)
            self.finish()



class ThreadingServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

    def __init__(self, server_address, target_url: str, verify: bool = True):
        self.target_url = target_url
        self.verify = verify
        HTTPServer.__init__(self, server_address, RequestHandler, True)

    def on_connected(self, connection: Connection):
        print("connection " + str(connection) + " established")

    def on_disconnected(self, connection: Connection):
        print("connection " + str(connection) + " terminated")


def run_server(port: int, target_url: str, verify: bool = True):
    server = ThreadingServer(('0.0.0.0', port), target_url, verify)
    print(f"Starting httpd server on {port}")
    server.serve_forever()

