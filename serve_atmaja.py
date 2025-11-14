from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class RedirectHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Redirect / or /index.html to the main homepage
        if self.path in ('/', '/index.html'):
            self.send_response(301)
            self.send_header('Location', '/atmaja_website_redesign.html')
            self.end_headers()
        else:
            # Serve all other files normally
            super().do_GET()

if __name__ == "__main__":
    # Change directory to where your files are located
    os.chdir('/Users/tanisha/Desktop/atmaja')

    # Run the server on localhost:8000
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RedirectHandler)
    print("🌐 Serving Atmaja website at: http://localhost:8000")
    print("➡️  Automatically redirects /index.html to /atmaja_website_redesign.html")
    print("Press CTRL+C to stop the server.")
    httpd.serve_forever()
