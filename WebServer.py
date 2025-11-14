from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP request by returning a fixed 'page'.'''

    PAGE = '''\
<html>
<body>
<table>
<tr>  <td>Header</td>         <td>Value</td>          </tr>
<tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
<tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
<tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
<tr>  <td>Command</td>        <td>{command}</td>      </tr>
<tr>  <td>Path</td>           <td>{path}</td>         </tr>
</table>
</body>
</html>
'''
        



    def do_GET(self):
        PAGE = self.create_page()
        self.send_page(PAGE)
    
    def create_page(self):
        values = {
            'date_time'     : self.date_time_string(),
            'client_host'   : self.client_address[0],
            'client_port'   : self.client_address[1],
            'command'       : self.command,
            'path'          : self.path
        }
        return self.PAGE.format(**values)
    

    # Handle a GET Request
    def send_page(self, PAGE: str) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        body = PAGE.encode("utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

#----------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
