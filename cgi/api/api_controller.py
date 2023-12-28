import logging;
logging.basicConfig(
    filename="debug.log", 
    level=logging.INFO, 
    format="%(asctime)s %(levelname)s [%(filename)s::%(lineno)d] %(message)s %(args)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)

import json
import os
import re
import base64

class ApiController():
    def send_response(self, status_code: int = 200, reason_phrase: str = 'OK', body: object = None, meta: object = None, data: object = None):
        status_header = f"Status: {status_code}"
        if reason_phrase:
            status_header += f" {reason_phrase}"
        print(status_header)
        print("Content-Type: application/json")
        print("")
        if body:
            print(json.dumps(body), end="")
        else:
            print(json.dumps({'meta': meta, 'data': data}), end="")
        exit(0)

    def serve(self):
        method = os.environ['REQUEST_METHOD']
        action = f"do_{method.lower()}"
        attr = getattr(self, action, None)
        if attr:
            attr()
        else:
            self.send_response(501, "Not Implemented")

    def get_auth_header_or_exit(self, auth_scheme: str):
        auth_header_name = 'HTTP_AUTHORIZATION'

        if not auth_scheme.endswith(" "):
            auth_scheme += ' '

        if not auth_header_name in os.environ:
            self.send_response(401, 'Unauthorized', {'message': "Missing 'Authorization' header"})
        
        auth_header_value = os.environ[auth_header_name]
        if not auth_header_value.startswith(auth_scheme):
            self.send_response(401, 'Unauthorized', {'message': f"Invalid Authorization scheme: '{auth_scheme}' only"})

        auth_token = auth_header_value[len(auth_scheme):]
        return auth_token
    
    def get_bearer_token_or_exit(self):
        auth_token = self.get_auth_header_or_exit('Bearer ')
        if not re.match("^[0-9a-f-]+$", auth_token):
            self.send_response(401, 'Unauthorized', {'message': "Invalid Authorization token: hexadecimal form expected"})

        return auth_token


    def get_basic_credentials_or_exit(self):
        auth_token = self.get_auth_header_or_exit('Basic ')

        try:
            decoded = base64.b64decode(auth_token, validate=True).decode()
            login, password = decoded.split(':', 1)
            return (login, password)
        except:
            self.send_response(401, 'Unauthorized', {'message': 'Malformed credentials: Basic scheme required'})

        return auth_token