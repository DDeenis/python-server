from starter import MainHandler

class HomeController():
    def __init__(self, handler: MainHandler):
        self.handler = handler

    def index(self):
        self.handler.session['data'] = 'HomeController'
        self.view_data = {
            '@session-timestamp': self.handler.session['timestamp']
        }
        self.handler.send_view()
    
    def about(self):
        self.handler.send_view()
    
    def privacy(self, handler: MainHandler):
        handler.send_response(200, 'OK')
        handler.send_header('Content-Type', 'text/html; charset=utf-8')
        handler.end_headers()
        handler.wfile.write('<h1>Privacy page</h1>'.encode())