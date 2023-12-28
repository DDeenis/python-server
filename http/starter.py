from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import random
import appconfig
import inspect
import importlib
import routes
import time
import json

class MainHandler(BaseHTTPRequestHandler):
    sessions = {}

    def __init__(self, request, client_address, server) -> None:
        self.response_headers = dict()
        self.session = dict()
        super().__init__(request, client_address, server)

    def do_GET(self):
        cookies_header = self.headers.get('Cookie', '')
        cookies = dict(cookie.split('=') for cookie in cookies_header.split('; ') if '=' in cookie);
        session_id = str(cookies['session-id']);

        if 'session-id' in cookies and session_id in MainHandler.sessions:
            self.session = MainHandler.sessions[session_id]
        else:
            while True:
                session_id = str(random.randint(0, 99999))
                if not session_id in MainHandler.sessions: break
            self.response_headers['Set-Cookie'] = f'session-id={session_id}; Path=/;'
            MainHandler.sessions[session_id] = {
                'id': session_id,
                'timestamp': time.time()
            }
            self.sessions = MainHandler.sessions[session_id]

        parts = self.path.split('?')
        path = parts[0]
        query_string = parts[1] if len(parts) > 1 else None

        if '../' in path or '..\\' in path:
            self.send_404()
            return
         
        filename = appconfig.WWWROOT_PATH + self.path
        if os.path.isfile(filename):
            self.flush_file(filename)
            return

        path_params = routes.parse_path(path)
        controller = path_params['controller']
        action = path_params['action']

        try:
            controller_module = importlib.import_module(controller)
            controller_class = getattr(controller_module, controller)
            controller_instance = controller_class(self)
            controller_action = getattr(controller_instance, action)
        except Exception as err:
            print(err)
            controller_action = None

        if controller_action:
            controller_action()
        else:
            self.send_404();
    
    def flush_file(self, filename: str):
        if not os.path.isfile(filename):
            return self.send_404()

        ext = filename.split('.')[-1]
        if ext in ('css', 'html'):
            content_type = 'text/' + ext
        elif ext == 'js':
            content_type = 'text/javascript'
        elif ext == 'ico':
            content_type = 'image/x-icon'
        elif ext in ('png', 'bmp'):
            content_type = 'image/' + ext
        elif ext in ('jpg', 'jpeg'):
            content_type = 'image/jpeg'
        elif ext in ('py', 'ini', 'env', 'jss', 'php'):
            self.send_404()
            return
        else:
            content_type = "application/octet-stream"

        self.send_response(200, 'OK')
        self.send_header('Content-Type', content_type)
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())

    def send_404(self):
        self.send_response(404, 'Not Found')
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write('Resource not found'.encode())

    def send_view(self, view_name: str = None, layout_name: str = None):
        prev_frame = inspect.currentframe().f_back
        controller_instance = prev_frame.f_locals['self']

        if layout_name == None:
            layout_name = appconfig.DEFAULT_VIEW
        
        if view_name == None:
            action_name = prev_frame.f_code.co_name;
            controller_short_name = controller_instance.__class__.__name__.removesuffix('Controller').lower()
            view_name = f"{appconfig.VIEWS_PATH}/{controller_short_name}/{action_name}.html"

        if not os.path.isfile(layout_name) or not os.path.isfile(view_name):
            return self.send_404()
        
        for k, v in self.session.items():
            MainHandler.sessions[self.session['id']][k] =v
        
        self.send_response(200, 'OK')
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        for header, value in self.response_headers.items():
            self.send_header(header, value)
        self.end_headers()
        with open(view_name) as view:
            view_content = view.read()
            view_data = getattr(controller_instance, 'view_data', None)
            if view_data:
                for k, v in view_data.items():
                    view_content = view_content.replace(k, str(v))
            with open(layout_name) as layout:
                page_content = layout.read().replace("<!-- RenderBody -->", view_content).encode('cp1251')
                self.wfile.write(page_content)

    def log_request(self, code: int | str = "-", size: int | str = "-") -> None:
        # return super().log_request(code, size)
        return None

def main():
    if os.path.exists('sessions.json'):
        with open('sessions.json', 'r') as f:
            MainHandler.sessions = json.load(f)

    http_server = HTTPServer(('localhost', 3000), MainHandler)
    try:
        print("Server starting")
        http_server.serve_forever()
    except:
        print("Server stopped")
        with open('sessions.json', 'w') as f:
                    json.dump(MainHandler.sessions, f)

if __name__ == "__main__":
    main()