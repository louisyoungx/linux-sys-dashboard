#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import subprocess
import argparse

from settings import PORT, HOST

try:
    from SocketServer import ThreadingMixIn
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from socketserver import ThreadingMixIn
    from http.server import HTTPServer, BaseHTTPRequestHandler


parser = argparse.ArgumentParser(description='Simple Threaded HTTP server to run Linux-sys Dashboard.')
parser.add_argument('--port', metavar='PORT', type=int, nargs='?', default=PORT,
                    help='Port to run the server on.')

modulesSubPath = '/linux_json_api.sh'
appRootPath = os.path.dirname(os.path.realpath(__file__))

class MainHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            data = ''
            contentType = 'text/html'
            if self.path.startswith("/server/"):
                contentType = 'json'
                module = self.path.split('=')[1]
                cmdPath = appRootPath + modulesSubPath + " " + module
                output = subprocess.Popen(
                    "sudo " + cmdPath,
                    shell = True,
                    stdout = subprocess.PIPE)
                data = output.communicate()[0]
                self.send_response(200)
                self.send_header('Content-type', contentType)
                self.end_headers()
                self.wfile.write(data)
            else:
                if self.path == '/':
                    self.path = '/index.html'
                elif self.path == '/favicon.ico':
                    self.path = '/favicon.svg'
                f = open(appRootPath + '/static' + self.path)
                data = f.read()
                if self.path.startswith('/linuxDash.min.css'):
                    contentType = 'text/css'
                if self.path.startswith('/favicon.svg'):
                    contentType = 'image'
                f.close()
                self.send_response(200)
                self.send_header('Content-type', contentType)
                self.end_headers()
                self.wfile.write(data.encode(encoding='UTF-8'))

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

if __name__ == '__main__':
    args = parser.parse_args()
    server = ThreadedHTTPServer((HOST, args.port), MainHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
