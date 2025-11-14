#!/usr/bin/env python3
"""
Simple HTTP server with no-cache headers to prevent browser caching during development
"""
import http.server
import socketserver
from functools import partial

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

PORT = 8000

with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Cache headers disabled - you'll see live changes")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()
